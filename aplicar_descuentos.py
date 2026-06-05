from supabase import create_client
from dotenv import load_dotenv
import pandas as pd
import os

# Cargar variables de entorno
load_dotenv()

# Conectar a Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Obtener productos
response = supabase.table("productos").select("*").execute()

# Convertir a DataFrame
df = pd.DataFrame(response.data)

print("PRODUCTOS ORIGINALES:")
print(df[["id", "nombre", "precio", "stock"]])

# Aplicar descuento del 10% a productos con stock > 10
df.loc[df["stock"] > 10, "precio"] = (
    df.loc[df["stock"] > 10, "precio"] * 0.90
).round(2)

print("\nPRODUCTOS CON DESCUENTO:")
print(df[["id", "nombre", "precio", "stock"]])

# Actualizar en Supabase
for _, fila in df.iterrows():

    supabase.table("productos").update({
        "precio": float(fila["precio"])
    }).eq(
        "id",
        int(fila["id"])
    ).execute()

print("\nDescuentos aplicados correctamente.")