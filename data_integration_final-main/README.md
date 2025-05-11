# Food Inspection Violation

## Description

Ce projet analyse les données d'inspection alimentaire en utilisant Kafka, HDFS, Spark et SQLite. Il met en œuvre un pipeline complet de traitement des données : collecte, stockage, nettoyage, calcul des métriques et versionnement.

Le but est de démontrer comment manipuler de grandes quantités de données en intégrant plusieurs technologies pour garantir robustesse et efficacité.

---

## Architecture

- **Kafka** : Gère les flux de données avec un producer/consumer à partir du fichier `Food_Facility_RestaurantInspections.csv`.
- **HDFS** : Stocke les fichiers `Geocoded_FoodFacilities.csv` et `Food_Facility_RestaurantInspections_split.csv`.
- **SQLite** : Contient les données nettoyées et transformées.
- **Spark** : Effectue les transformations, les nettoyages et les jointures.
- **Versionnement** : Archive les résultats finaux pour traçabilité.

---

## Fonctionnalités

- Création de topics Kafka et gestion des flux.
- Stockage et manipulation des données dans HDFS.
- Nettoyage et jointure des données avec Spark.
- Calcul de métriques analytiques clés.
- Versionnement des données finales.

---

## Prérequis

1. **Outils nécessaires** :
   - Python 3.9+
   - Docker et Docker Compose
   - Hadoop (HDFS)
   - Spark
   - SQLite

2. **Installation des dépendances** :
   ```bash
   pip install -r requirements.txt
docker-compose up -d
├── bdd/
│   ├── setup_db.py
├── config/
│   ├── kafka_config.json
├── data/
│   ├── Food_Facility_RestaurantInspections.csv
│   ├── FoodFacilityRestaurantInspectionViolations.csv
│   ├── Geocoded_FoodFacilities.csv
│   ├── clean_joined_data.py
├── hdfs/
│   ├── hdfs_to_sqlite.py
│   ├── joinall.py
│   ├── read_geocoded_facilities.py
│   ├── read_inspections.py
├── kafka_scripts/
│   ├── create_topic.py
│   ├── producer.py
│   ├── consumer.py
├── metrics/
│   ├── calculate_metrics.py
├── versionning/
│   ├── save_version.sh
│   ├── version_XXXXXX.zip
├── myenv/
├── requirements.txt
├── docker-compose.yml
├── README.md

docker-compose up -d
python kafka_scripts/create_topic.py
python kafka_scripts/producer.py
python kafka_scripts/consumer.py

hdfs dfs -put data/Geocoded_FoodFacilities.csv /data
hdfs dfs -put data/Food_Facility_RestaurantInspections_split.csv /data

python hdfs/joinall.py
python data/clean_joined_data.py

python metrics/calculate_metrics.py
bash versionning/save_version.sh

Résultats
Données SQLite : Stockées dans kafka_data.db.
Métriques : Résultats analytiques détaillés.
Archives Versionnées : Dans le dossier versionning/

pip install werkzeug==2.0.3 markupsafe==2.0.1
Modifier core-site.xml pour utiliser l'IP du conteneur au lieu de localhost

docker-compose down && docker-compose up -d

Auteurs
Ossama & Manel : Contributeur principal.


Collez ce contenu dans un fichier nommé `README.md` à la racine de votre projet et ajoutez-le à votre dépôt GitHub.


