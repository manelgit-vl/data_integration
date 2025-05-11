from pyspark.sql import SparkSession
import sqlite3

# Créer une session Spark
spark = SparkSession.builder \
    .appName("HDFS to SQLite") \
    .getOrCreate()

# Chemins des fichiers HDFS
hdfs_file1 = "hdfs://localhost:9000/test/Food_Facility_RestaurantInspections.csv"
hdfs_file2 = "hdfs://localhost:9000/test/Geocoded_FoodFacilities.csv"

# Lire les fichiers CSV depuis HDFS
df1 = spark.read.option("header", "true").csv(hdfs_file1)
df2 = spark.read.option("header", "true").csv(hdfs_file2)

# Chemin de la base SQLite
sqlite_db_path = "/Users/ossama/Documents/food-inspection-violation/kafka_data.db"

# Noms des tables SQLite
table_name1 = "restaurant_inspections"
table_name2 = "geocoded_facilities"

# Fonction pour sauvegarder directement dans SQLite
def save_to_sqlite_directly(df, table_name):
    # Convertir le DataFrame Spark en DataFrame Pandas
    df_pd = df.toPandas()
    
    # Insérer directement dans SQLite
    with sqlite3.connect(sqlite_db_path) as conn:
        df_pd.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Table '{table_name}' insérée avec succès dans SQLite.")

# Sauvegarder les DataFrames dans des tables distinctes
save_to_sqlite_directly(df1, table_name1)
save_to_sqlite_directly(df2, table_name2)

# Arrêter la session Spark
spark.stop()
