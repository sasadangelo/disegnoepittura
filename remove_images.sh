#!/bin/bash

# Trova tutti i file con spazio finale nella lista di changes not staged
git status --porcelain | while read -r status file; do
    # rimuove eventuali escape e virgolette
    trimmed_file=$(echo "$file" | sed 's/^ *//; s/ *$//')
    # se finisce con spazio (ASCII 32)
    if [[ "$file" =~ [[:space:]]$ ]]; then
        echo "Rimuovo file con spazio finale: '$file'"
        git rm -- "$file"
    fi
done
