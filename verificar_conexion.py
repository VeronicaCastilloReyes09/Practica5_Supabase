from supabase import create_client
from dotenv import load_dotenv
import os
load_dotenv() # Carga las variables del .env
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
supabase = create_client(url, key)
print('Conexion exitosa a Supabase')
print(f'URL: {url}')