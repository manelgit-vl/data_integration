from confluent_kafka.admin import AdminClient, NewTopic



# Charger la configuration Kafka
config = {
    "bootstrap.servers": "192.168.1.166:9092"  # Mets à jour si nécessaire
}

# Créer un client administrateur
admin_client = AdminClient(config)

# Définir le topic à créer
topic_name = "food_inspection_violations"
topic = NewTopic(topic_name, num_partitions=1, replication_factor=1)

try:
    # Créer le topic
    admin_client.create_topics([topic])
    print(f"Topic '{topic_name}' created successfully!")
except Exception as e:
    print(f"Failed to create topic: {e}")
