import re
from pathlib import Path
from PIL import Image

# Percorso del file markdown
base_folder = Path(__file__).parent.resolve()
md_file = base_folder / "_posts/2019-12-08-chiaroscuro.md"
md_text = md_file.read_text(encoding="utf-8")

# Trova tutti i percorsi delle immagini locali (senza query string)
image_paths = re.findall(r'src=".*?(/wp-content/uploads/[^"?]+)', md_text)

for rel_path in image_paths:
    img_path = base_folder / rel_path[1:]  # rimuove lo slash iniziale
    if not img_path.exists():
        print(f"[WARN] Immagine non trovata: {img_path}")
        continue

    webp_path = img_path.with_suffix(".webp")

    # Converti in webp
    with Image.open(img_path) as img:
        img.save(webp_path, "WEBP", quality=80)

    # Rimuovi l'immagine originale
    img_path.unlink()

    # Aggiorna il markdown: cambia estensione e rimuove query string
    md_text = re.sub(
        re.escape(rel_path) + r"(\?v=\d+)?",
        str(rel_path).replace(img_path.suffix, ".webp"),
        md_text,
    )

# Salva il markdown aggiornato
md_file.write_text(md_text, encoding="utf-8")

print("Conversione completata!")
