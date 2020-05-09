# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS goods
                           (product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            kat_name TEXT,
                            price TEXT,
                            photo TEXT             
                             )
                          """)
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS company
                           (
                            company_id TEXT,
                            company_name TEXT,
                            latitude TEXT,
                            longitude TEXT,
                            phone_number TEXT            
                             )
                          """)
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS "user"
                            ( chat_id TEXT,
                            first_name TEXT,
                            last_name TEXT, 
                            ph_number TEXT,
                            seller BLOB                                  
                             )
                          """)
conn.commit()
conn.close()


