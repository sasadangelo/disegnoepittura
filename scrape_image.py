import os
import requests
import re
from pathlib import Path

# Configurazione
POSTS_DIR = "_posts"
UPLOADS_DIR = "wp-content/uploads"  # qui salviamo le immagini
WORDPRESS_URL = "https://www.disegnoepittura.it"  # URL base del tuo WordPress

# Crea la cartella uploads se non esiste
Path(UPLOADS_DIR).mkdir(parents=True, exist_ok=True)


def download_image(url):
    """
    Scarica un'immagine da URL e la salva nella cartella corretta.
    Restituisce il path locale relativo.
    """
    local_path = os.path.join(UPLOADS_DIR, url.replace("/wp-content/uploads/", ""))
    local_dir = os.path.dirname(local_path)
    os.makedirs(local_dir, exist_ok=True)

    # SKIP se il file esiste già
    if os.path.exists(local_path):
        print(f"Esiste già, skip: {local_path}")
        return local_path

    full_url = f"{WORDPRESS_URL}{url}"
    try:
        r = requests.get(full_url, stream=True)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        print(f"Scaricata: {local_path}")
        return local_path
    except requests.RequestException as e:
        print(f"Errore nel download di {full_url}: {e}")
        return None


def process_post_file(filepath):
    """
    Aggiorna tutti i riferimenti alle immagini in un post Markdown.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Cerca tutti i src delle immagini che contengono wp-content/uploads
    matches = re.findall(r'(/wp-content/uploads/[^)"\']+)', content)
    for match in matches:
        local_path = download_image(match)
        if local_path:
            # sostituisce il riferimento originale con quello locale
            content = content.replace(match, "/" + local_path.replace("\\", "/"))

    # Riscrivi il file con i riferimenti aggiornati
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Aggiornato: {filepath}")


def main():
    # Cicla su tutti i post Markdown
    for root, dirs, files in os.walk(POSTS_DIR):
        for filename in files:
            if filename.endswith((".md", ".markdown")):
                filepath = os.path.join(root, filename)
                process_post_file(filepath)


if __name__ == "__main__":
    main()
