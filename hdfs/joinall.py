import sqlite3

# Connexion à la base SQLite
conn = sqlite3.connect('/Users/ossama/Documents/food-inspection-violation/kafka_data.db')
cursor = conn.cursor()

# Requête SQL pour la jointure
query = """
SELECT 
    r._id,
    r.encounter,
    r.id AS inspection_id,
    r.placard_st AS inspection_placard_st,
    r.placard_desc AS inspection_placard_desc,
    r.facility_name AS inspection_facility_name,
    r.bus_st_date AS inspection_bus_st_date,
    r.category_cd AS inspection_category_cd,
    r.description AS inspection_description,
    r.num AS inspection_num,
    r.street AS inspection_street,
    r.city AS inspection_city,
    r.state AS inspection_state,
    r.zip AS inspection_zip,
    r.inspect_dt AS inspection_inspect_dt,
    r.start_time AS inspection_start_time,
    r.end_time AS inspection_end_time,
    r.municipal AS inspection_municipal,
    g.facility_name AS geocoded_facility_name,
    g.num AS geocoded_num,
    g.street AS geocoded_street,
    g.city AS geocoded_city,
    g.state AS geocoded_state,
    g.zip AS geocoded_zip,
    g.category_cd AS geocoded_category_cd,
    g.description AS geocoded_description,
    g.x AS geocoded_x,
    g.y AS geocoded_y,
    g.address AS geocoded_address,
    k.encounter AS kafka_encounter,
    k.facility_name AS kafka_facility_name,
    k.description_new AS kafka_description_new,
    k.rating AS kafka_rating,
    k.low AS kafka_low,
    k.medium AS kafka_medium,
    k.high AS kafka_high,
    k.url AS kafka_url
FROM 
    restaurant_inspections r
LEFT JOIN 
    geocoded_facilities g
ON 
    r._id = g._id
LEFT JOIN 
    kafka_data k
ON 
    r._id = k._id;
"""

# Exécuter la requête
cursor.execute(query)

cursor.execute("CREATE TABLE IF NOT EXISTS joined_data AS " + query)

# Récupérer les résultats
results = cursor.fetchall()

# Afficher les résultats
for row in results:
    print(row)

# Fermer la connexion
conn.close()
