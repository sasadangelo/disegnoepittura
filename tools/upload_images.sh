#!/bin/bash

UPLOADS_DIR="wp-content/uploads"

# Lista tutti i file non tracciati da git
untracked_files=$(git ls-files --others --exclude-standard "$UPLOADS_DIR")

echo "File untracked trovati:"
echo "$untracked_files"
echo

# Cicla su ogni file
while IFS= read -r file; do
    # Controlla se il file finisce con spazio
    if [[ "$file" =~ [[:space:]]$ ]]; then
        echo "Rimuovo file con spazio finale: '$file'"
        git rm -- "$file"
    else
        echo "Aggiungo file: '$file'"
        git add -- "$file"
    fi
done <<< "$untracked_files"
