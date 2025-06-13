#!/bin/bash

# Vérifier les arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <ancien_nom_package> <nouveau_nom_package> <dossier_racine>"
    exit 1
fi

# Arguments
OLD_PACKAGE_NAME=$1
NEW_PACKAGE_NAME=$2
ROOT_DIR=$3

echo "Renommage du package ROS de '$OLD_PACKAGE_NAME' à '$NEW_PACKAGE_NAME' dans le dossier '$ROOT_DIR'"

# Renommer le dossier du package si son nom est identique à l'ancien package
if [ -d "$ROOT_DIR/$OLD_PACKAGE_NAME" ]; then
    echo "Renommage du dossier de package $OLD_PACKAGE_NAME -> $NEW_PACKAGE_NAME"
    mv "$ROOT_DIR/$OLD_PACKAGE_NAME" "$ROOT_DIR/$NEW_PACKAGE_NAME"
fi

# Modifier uniquement le nom du package dans 'package.xml' et certaines lignes de 'CMakeLists.txt'
echo "Modification des fichiers package.xml et CMakeLists.txt"

# Modifier les fichiers 'package.xml' pour changer le nom du package
find "$ROOT_DIR/$NEW_PACKAGE_NAME" -type f -name "package.xml" -exec sed -i "s/<name>$OLD_PACKAGE_NAME<\/name>/<name>$NEW_PACKAGE_NAME<\/name>/g" {} +

# Modifier les occurrences spécifiques dans 'CMakeLists.txt'
# Eviter de toucher aux noms de fichiers et variables non pertinents
find "$ROOT_DIR/$NEW_PACKAGE_NAME" -type f -name "CMakeLists.txt" -exec sed -i "s/\b$OLD_PACKAGE_NAME\b/$NEW_PACKAGE_NAME/g" {} +

# Rechercher tous les fichiers dans l'arborescence (y compris les launch files) et remplacer les occurrences du nom du package
echo "Modification des appels au package dans l'arborescence"
find "$ROOT_DIR" -type f -exec grep -l "$OLD_PACKAGE_NAME" {} + | while read -r file; do
    echo "Modification de $file"
    # Remplacer uniquement les mots exacts (noms de package) dans les fichiers
    sed -i "s/\b$OLD_PACKAGE_NAME\b/$NEW_PACKAGE_NAME/g" "$file"
done

echo "Renommage terminé OK. "
