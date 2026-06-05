from supabase import create_client
from dotenv import load_dotenv
import pandas as pd
import os
load_dotenv()
supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
TABLAS = ['usuarios', 'productos', 'pedidos']
for tabla in TABLAS:
	response = supabase.table(tabla).select('*').execute()
	df = pd.DataFrame(response.data)
	df.to_csv(f'backup_{tabla}.csv', index=False)
	print(f'Tabla {tabla} descargada - {len(df)} registros')