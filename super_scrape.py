import os
import re
import requests
from datetime import datetime
from markdownify import markdownify as md
from slugify import slugify
from urllib.parse import urljoin
from pathlib import Path
from urllib.parse import urlparse

# --- CONFIG ---
WP_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/posts"
PAGE_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/pages"
CATEGORY_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/categories"
TAG_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/tags"

POSTS_DIR = "_posts"
PAGES_DIR = "_pages"
UPLOADS_DIR = "wp-content/uploads"

WORDPRESS_URL = "https://www.disegnoepittura.it"

# Crea le cartelle se non esistono
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)
Path(UPLOADS_DIR).mkdir(parents=True, exist_ok=True)


def get_local_path_from_url(url):
    """
    Dall'URL completo di WordPress ricava il path locale sotto wp-content/uploads
    """
    parsed = urlparse(url)
    # parsed.path = /wp-content/uploads/13-Disegno-Inchiostrato-2-mini.jpg
    rel_path = parsed.path.lstrip("/")  # rimuove il primo /
    local_path = os.path.join(UPLOADS_DIR, *rel_path.split("/")[2:])
    # prendi solo la parte dopo 'wp-content/uploads/'
    return local_path


# --- UTILITY ---
def download_image(url):
    """
    Scarica immagine da URL e la salva in wp-content/uploads.
    Se esiste già, la salta.
    """
    # calcola il percorso locale corretto
    local_path = get_local_path_from_url(url)

    # skip se esiste già
    if os.path.exists(local_path):
        print(f"Esiste già, skip: {local_path}")
        return local_path

    # crea le cartelle se non ci sono
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    local_dir = os.path.dirname(local_path)
    os.makedirs(local_dir, exist_ok=True)

    if os.path.exists(local_path):
        # Skip se già presente
        return local_path

    # Controlla se url è già completo
    if url.startswith("http://") or url.startswith("https://"):
        full_url = url
    else:
        full_url = f"{WORDPRESS_URL}{url}"

    try:
        r = requests.get(full_url, stream=True)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print(f"Scaricata immagine: {local_path}")
        return local_path
    except requests.RequestException as e:
        print(f"Errore download immagine {full_url}: {e}")
        return None


def get_category_name(cat_id):
    r = requests.get(urljoin(CATEGORY_API_URL + "/", str(cat_id)))
    if r.status_code == 200:
        return r.json().get("name", str(cat_id))
    return str(cat_id)


def get_tag_name(tag_id):
    r = requests.get(urljoin(TAG_API_URL + "/", str(tag_id)))
    if r.status_code == 200:
        return r.json().get("name", str(tag_id))
    return str(tag_id)


def fetch_items(api_url):
    """Recupera post o pagine da WP REST API con paginazione."""
    items = []
    page = 1
    while True:
        print(f"Fetch: {api_url}, per_page: 100, page: {page}, _embed: true")
        r = requests.get(
            api_url, params={"per_page": 100, "page": page, "_embed": "true"}
        )
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        items.extend(data)
        page += 1
    return items


def process_content_images(content_md):
    """Scarica immagini referenziate nel contenuto e aggiorna path locali."""
    matches = re.findall(r'(/wp-content/uploads/[^)"\']+)', content_md)
    for match in matches:
        local_path = download_image(match)
        if local_path:
            content_md = content_md.replace(match, "/" + local_path.replace("\\", "/"))
    return content_md


def create_markdown_file(item, directory):
    """Crea il file markdown per un post o una pagina."""
    title = item["title"]["rendered"]
    date = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S")
    slug = item.get("slug") or slugify(title)

    # categorie e tag
    categories = [get_category_name(c) for c in item.get("categories", [])]
    tags = [get_tag_name(t) for t in item.get("tags", [])]

    # contenuto Markdown
    content_html = item["content"]["rendered"]
    content_md = md(content_html, heading_style="ATX")
    content_md = process_content_images(content_md)

    # featured image
    header_image = ""
    if item.get("featured_media") and item.get("_embedded"):
        try:
            media = item["_embedded"]["wp:featuredmedia"][0]
            media_url = media["source_url"]
            header_image = download_image(media_url)
        except (KeyError, IndexError):
            pass

    # front matter Minimal Mistakes
    front_matter = "---\n"
    front_matter += f'title: "{title}"\n'
    front_matter += f"date: {date.strftime('%Y-%m-%d %H:%M:%S')}\n"
    front_matter += f"categories: {categories}\n"
    front_matter += f"tags: {tags}\n"
    front_matter += "layout: single\n"
    if header_image:
        front_matter += f"header:\n  image: {header_image}\n"
    front_matter += "---\n\n"

    filename = os.path.join(directory, f"{date.strftime('%Y-%m-%d')}-{slug}.md")
    if os.path.exists(filename):
        print(f"Esiste già, skip: {filename}")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + content_md)
    print(f"Creato: {filename}")


def fix_baseurl_links(directory):
    """
    Cicla tutti i file markdown nella cartella e sostituisce
    /wp-content/... con {{ site.baseurl }}/wp-content/...
    """
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith((".md", ".markdown")):
                filepath = os.path.join(root, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Sostituzione dei link
                new_content = re.sub(
                    r'(/wp-content/uploads/[^)"\']+)', r"{{ site.baseurl }}\1", content
                )

                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Aggiornati link in: {filepath}")
                else:
                    print(f"Nessuna modifica per: {filepath}")


# --- ESECUZIONE ---
# print("Scaricando post...")
# posts = fetch_items(WP_API_URL)
# for post in posts:
#     create_markdown_file(post, POSTS_DIR)

# print("Scaricando pagine...")
# pages = fetch_items(PAGE_API_URL)
# for page in pages:
#     create_markdown_file(page, PAGES_DIR)

# --- Correzione link baseurl ---
print("Aggiornando link /wp-content/... in {{ site.baseurl }}/wp-content/...")
fix_baseurl_links(POSTS_DIR)
fix_baseurl_links(PAGES_DIR)
print("Correzione completata!")

print("Completato!")
