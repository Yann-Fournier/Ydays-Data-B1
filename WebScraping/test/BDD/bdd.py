import sqlite3

# Connection à une base de données
conn = sqlite3.connect('ma_base.db')


# Creer une table

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom TEXT,
     age INTERGER
)
""")
conn.commit()

# Inserer des données
cursor.execute("""
INSERT INTO users(nom, age) VALUES(?, ?)""", ("olivier", 30))
#conn.commit()

# Recuperer l'id de la donnée que je viens de rentrée
id = cursor.lastrowid
print('dernier id: %d' % id)

conn.commit()
cursor.execute("SELECT * FROM users")
for row in cursor:
     print(row)




conn.close()