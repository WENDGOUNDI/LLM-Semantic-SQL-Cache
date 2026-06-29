## Library Importation
import sqlite3

# DB and table names definition
mydb = "enter the name of the sqlite database"
table_to_be_cleaned = "enter the name of the table to be cleaned"


conn = sqlite3.connect(mydb)
conn.cursor().execute(f"DROP TABLE IF EXISTS {table_to_be_cleaned}")
conn.commit()
conn.close()
print(f"🗑️ {table_to_be_cleaned} is purged cleanly.")