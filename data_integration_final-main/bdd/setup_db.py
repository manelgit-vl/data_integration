import sqlite3

# Connexion à SQLite
conn = sqlite3.connect('kafka_data.db')
cursor = conn.cursor()

# Supprimer la table existante si elle est incorrecte (facultatif)
cursor.execute('DROP TABLE IF EXISTS kafka_data')

# Création de la table kafka_data avec 22 colonnes
cursor.execute('''
CREATE TABLE IF NOT EXISTS kafka_data (
    _id TEXT PRIMARY KEY,
    encounter TEXT,
    id TEXT,
    placard_st TEXT,
    facility_name TEXT,
    bus_st_date TEXT,
    description TEXT,
    description_new TEXT,
    num TEXT,
    street TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    inspect_dt TEXT,
    start_time TEXT,
    end_time TEXT,
    municipal TEXT,
    rating TEXT,
    low TEXT,
    medium TEXT,
    high TEXT,
    url TEXT
)
''')

# Confirmation de la création de la table
conn.commit()
print("Table kafka_data créée avec succès dans kafka_data.db")

# Fermeture de la connexion
conn.close()
