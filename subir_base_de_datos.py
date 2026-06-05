import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
conn = psycopg2.connect(
host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'),
dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'),
password=os.getenv('DB_PASSWORD'), sslmode='require'
)
cursor = conn.cursor()
df = pd.read_csv('backup_productos.csv')
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO productos (nombre, precio, categoria, stock)
    VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING
    ''', (row['nombre'], row['precio'], row['categoria'], row['stock']))
conn.commit()
print(f'{len(df)} registros subidos a Supabase')
cursor.close(); conn.close()