from confluent_kafka import Producer
import json
import time

# Charger la configuration Kafka
with open('/Users/ossama/Documents/food-inspection-violation/config/kafka_config.json') as f:
    config = json.load(f)

# Créer un producteur Kafka
producer_config = {
    'bootstrap.servers': config['bootstrap_servers']
}
producer = Producer(producer_config)

# Fonction de callback pour la confirmation de livraison
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Lire les données depuis le fichier CSV et envoyer par lots à Kafka
file_path = '/Users/ossama/Documents/food-inspection-violation/data/Food Facility:Restaurant Inspection Violations.csv'
with open(file_path, 'r') as f:
    lines = f.readlines()

batch_size = 50000
for i in range(0, len(lines), batch_size):
    batch = lines[i:i + batch_size]
    for line in batch:
        producer.produce(
            config['topic'],
            key=str(i),  # clé optionnelle
            value=line.strip(),
            callback=delivery_report
        )
    producer.flush()
    time.sleep(1)  # Pause de 1 seconde entre les lots
