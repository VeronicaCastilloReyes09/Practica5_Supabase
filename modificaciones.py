from supabase import create_client
from dotenv import load_dotenv
import os
load_dotenv()
sb = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
# CREATE: insertar nuevo registro
nuevo = sb.table('productos').insert({
'nombre': 'Laptop Gamer X500',
'precio': 18999.99, 'categoria': 'Electronica', 'stock': 15
}).execute()
print('INSERT:', nuevo.data)
# READ: leer con filtros
res = (sb.table('productos')
.select('id, nombre, precio, stock')
.eq('categoria', 'Electronica')
.gt('stock', 0)
.order('precio', desc=True)
.execute())
print('Productos:', res.data)
# UPDATE: actualizar campos
sb.table('productos').update({'precio': 17499.99, 'stock': 20}).eq('nombre', 'Laptop Gamer X500').execute()
# UPSERT: insertar o actualizar si existe
sb.table('productos').upsert({
'id': 1, 'nombre': 'Laptop X500 Ed. Especial',
'precio': 19999.00, 'stock': 5
}).execute()
# DELETE (descomentar para usar)
# sb.table('productos').delete().eq('id', 999).execute()