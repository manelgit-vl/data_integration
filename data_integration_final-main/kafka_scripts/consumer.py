import sqlite3
from confluent_kafka import Consumer, KafkaException
import json
import csv
from io import StringIO

# Charger la configuration Kafka
with open('/Users/ossama/Documents/food-inspection-violation/config/kafka_config.json') as f:
    kafka_config = json.load(f)

# Configuration du consommateur Kafka
consumer_config = {
    'bootstrap.servers': kafka_config['bootstrap_servers'],
    'group.id': 'test-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

# Nom du topic
topic_name = kafka_config['topic']

# Connexion à SQLite
conn = sqlite3.connect('kafka_data.db')
cursor = conn.cursor()

# Création de la table mise à jour si elle n'existe pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS kafka_data (
    _id INTEGER PRIMARY KEY,
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
conn.commit()

# S'abonner au topic Kafka
consumer.subscribe([topic_name])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                print(f"Fin du topic {msg.topic()} {msg.partition()}")
            else:
                print(f"Erreur consommateur: {msg.error()}")
        else:
            # Décodage du message Kafka
            record_value = msg.value().decode('utf-8')

            # Utiliser csv pour parser correctement les champs
            csv_reader = csv.reader(StringIO(record_value))
            for row in csv_reader:
                # Vérifier que le nombre de colonnes est correct
                if len(row) == 22:  # Le CSV contient 22 colonnes
                    # Vérifier l'existence de l'enregistrement dans la base
                    cursor.execute('SELECT COUNT(*) FROM kafka_data WHERE _id = ?', (row[0],))
                    exists = cursor.fetchone()[0]

                    if not exists:
                        cursor.execute('''
                        INSERT INTO kafka_data (
                            _id, encounter, id, placard_st, facility_name, bus_st_date, description, description_new,
                            num, street, city, state, zip, inspect_dt, start_time, end_time,
                            municipal, rating, low, medium, high, url
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', row)
                        conn.commit()
                    else:
                        print(f"Doublon détecté pour _id: {row[0]}, ligne ignorée.")
                else:
                    print(f"Ligne ignorée en raison d'un mauvais format : {row}")
except KeyboardInterrupt:
    print("Arrêt du consommateur.")
finally:
    # Fermer les connexions
    consumer.close()
    conn.close()
