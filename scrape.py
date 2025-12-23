import os
import requests
from datetime import datetime
from markdownify import markdownify as md
from slugify import slugify
from urllib.parse import urljoin

# --- CONFIG ---
WP_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/posts"
CATEGORY_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/categories"
TAG_API_URL = "https://www.disegnoepittura.it/wp-json/wp/v2/tags"

POSTS_DIR = "_posts"
IMAGES_DIR = "assets/images/posts"

# Crea le cartelle se non esistono
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)


# --- FUNZIONI ---
def download_image(url):
    filename = url.split("/")[-1].split("?")[0]  # rimuove query string
    filepath = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(filepath):
        r = requests.get(url)
        if r.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(r.content)
    return f"/{IMAGES_DIR}/{filename}"


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


def fetch_posts():
    posts = []
    page = 1
    while True:
        r = requests.get(WP_API_URL, params={"per_page": 100, "page": page})
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        posts.extend(data)
        page += 1
    return posts


def create_post_file(post):
    title = post["title"]["rendered"]
    date = datetime.strptime(post["date"], "%Y-%m-%dT%H:%M:%S")
    slug = post.get("slug") or slugify(title)

    # categorie e tag reali
    categories = [get_category_name(c) for c in post.get("categories", [])]
    tags = [get_tag_name(t) for t in post.get("tags", [])]

    # contenuto Markdown
    content_html = post["content"]["rendered"]
    content_md = md(content_html, heading_style="ATX")

    # featured image
    header_image = ""
    if post.get("featured_media") and post.get("_embedded"):
        try:
            media = post["_embedded"]["wp:featuredmedia"][0]
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

    filename = os.path.join(POSTS_DIR, f"{date.strftime('%Y-%m-%d')}-{slug}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter + content_md)
    print(f"Creato post: {filename}")


# --- ESECUZIONE ---
print("Scaricando post da WordPress...")
posts = fetch_posts()

for post in posts:
    create_post_file(post)

print("Scraping completato!")
