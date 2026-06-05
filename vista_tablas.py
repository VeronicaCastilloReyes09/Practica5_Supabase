import psycopg2, pandas as pd, os
from dotenv import load_dotenv
load_dotenv()
conn = psycopg2.connect(
host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'),
dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'),
password=os.getenv('DB_PASSWORD'), sslmode='require'
)
# 1. Listar todas las tablas publicas
df_tablas = pd.read_sql('''
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public' ORDER BY table_name
''', conn)
print(df_tablas.to_string(index=False))
# 2. Ver primeros 10 registros
df = pd.read_sql('SELECT * FROM productos LIMIT 10', conn)
print(df)
conn.close()