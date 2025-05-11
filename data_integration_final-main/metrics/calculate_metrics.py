import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
db_path = "kafka_data.db"  # Changez ce chemin si nécessaire
conn = sqlite3.connect(db_path)

# Charger les données de la table `joined_data`
query = "SELECT * FROM joined_data"
data = pd.read_sql_query(query, conn)

# Calculer le nombre total de violations par type
violations_by_type = data.groupby("inspection_category_cd").size().reset_index(name="total_violations")
print("\nNombre total de violations par type:")
print(violations_by_type)

# Calculer le nombre d'inspections par établissement
inspections_by_facility = data.groupby("inspection_facility_name").size().reset_index(name="total_inspections")
print("\nNombre d'inspections par établissement:")
print(inspections_by_facility)

# Localisation géographique des violations (nombre de violations par ville et état)
violations_by_location = data.groupby(["inspection_city", "inspection_state"]).size().reset_index(name="total_violations")
print("\nLocalisation géographique des violations:")
print(violations_by_location)

# Sauvegarder les métriques dans des fichiers CSV
violations_by_type.to_csv("violations_by_type.csv", index=False)
inspections_by_facility.to_csv("inspections_by_facility.csv", index=False)
violations_by_location.to_csv("violations_by_location.csv", index=False)

# Optionnel : Sauvegarder les métriques dans SQLite
violations_by_type.to_sql("violations_by_type", conn, if_exists="replace", index=False)
inspections_by_facility.to_sql("inspections_by_facility", conn, if_exists="replace", index=False)
violations_by_location.to_sql("violations_by_location", conn, if_exists="replace", index=False)

# Fermer la connexion à la base de données
conn.close()

print("\nLes métriques ont été calculées et sauvegardées dans des fichiers CSV et la base SQLite.")
