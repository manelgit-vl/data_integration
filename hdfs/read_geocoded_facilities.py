from pyspark.sql import SparkSession

def read_inspections(hdfs_path='data/Food_Facility_RestaurantInspections.csv'):
    """
    Lit le fichier Food Facility: Restaurant Inspections depuis HDFS.

    Args:
        hdfs_path (str): Le chemin HDFS du fichier (par exemple, hdfs://localhost:50070).

    Returns:
        pyspark.sql.DataFrame: Les données sous forme de DataFrame Spark.
    """
    try:
        # Création de la session Spark
        spark = SparkSession.builder \
            .appName("Read Food Inspections") \
            .getOrCreate()

        # Lecture du fichier depuis HDFS
        df = spark.read.format("csv") \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .load(hdfs_path)

        return df

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Food Facility:Restaurant Inspections: {e}")
        return None

if __name__ == "__main__":
    df = read_inspections()
    if df:
        df.show(5)
