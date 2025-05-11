import sqlite3

# Connexion à la base de données SQLite
db_path = "kafka_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Étape 1 : Identifier les colonnes contenant uniquement des NULL
cursor.execute("PRAGMA table_info(joined_data)")
columns_info = cursor.fetchall()
columns_to_drop = []

for column in columns_info:
    col_name = column[1]
    cursor.execute(f"SELECT COUNT(*) FROM joined_data WHERE {col_name} IS NOT NULL")
    non_null_count = cursor.fetchone()[0]
    if non_null_count == 0:
        columns_to_drop.append(col_name)

# Étape 2 : Supprimer les colonnes inutiles
for col in columns_to_drop:
    cursor.execute(f"ALTER TABLE joined_data DROP COLUMN {col}")
    print(f"Colonne supprimée : {col}")

# Étape 3 : Nettoyer les colonnes restantes (par exemple, retirer les doublons)
cursor.execute("""
DELETE FROM joined_data
WHERE ROWID NOT IN (
    SELECT MIN(ROWID)
    FROM joined_data
    GROUP BY _id, inspection_facility_name, inspection_zip
)
""")

# Étape 4 : Valider et fermer la connexion
conn.commit()
conn.close()

print("Nettoyage terminé.")
