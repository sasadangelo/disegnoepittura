#!/bin/bash

UPLOADS_DIR="wp-content/uploads"

# Cicla ricorsivamente tutti i file
find "$UPLOADS_DIR" -type f | while IFS= read -r file; do
    # Ottieni il nome del file senza il path
    base=$(basename "$file")
    dir=$(dirname "$file")

    # Controlla se il nome finisce con spazio
    if [[ "$base" =~ [[:space:]]$ ]]; then
        # Rimuove gli spazi finali
        new_base=$(echo "$base" | sed 's/[[:space:]]*$//')
        new_file="$dir/$new_base"

        # Rinominare il file
        mv "$file" "$new_file"
        echo "Rinominato: '$file' -> '$new_file'"
    fi
done
