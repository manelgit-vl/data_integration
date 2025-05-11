#!/bin/bash

# Nom du dossier contenant vos sauvegardes
BACKUP_DIR="versionning"

# Nom du projet à sauvegarder
PROJECT_DIR="$HOME/Documents/food-inspection-violation"

# Date pour identifier la version
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

# Nom de la version
ZIP_NAME="version_${DATE}.zip"

# Créer le dossier de sauvegarde s'il n'existe pas
mkdir -p $BACKUP_DIR

# Créer l'archive ZIP en excluant les fichiers inutiles
zip -r "$BACKUP_DIR/$ZIP_NAME" "$PROJECT_DIR" -x "$PROJECT_DIR/myenv/*" "$PROJECT_DIR/*.db" "$PROJECT_DIR/*.tar.gz"

# Afficher un message de confirmation
echo "Version sauvegardée dans $BACKUP_DIR/$ZIP_NAME"

