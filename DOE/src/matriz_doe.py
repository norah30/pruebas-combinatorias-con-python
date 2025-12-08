# Generación de Matriz DOE

from pyDOE3 import fullfact
import pandas as pd

# Definir factores y niveles
niveles = [4, 5, 3, 5, 5]

# Generación de la matriz factorial completa
matriz = fullfact(niveles).astype(int) 

# Factores y sus valores
factores = {
    "Tipo de Cliente": ["Nuevo", "Premium", "Vip", "Corporativo"],
    "Método de Pago": ["Débito", "Crédito", "PayPal", "Transferencia", "Contra entrega"],
    "Tipo de Envío": ["Recogida en Tienda", " A Domicilio", "Internacional"],
    "Dispositivo": ["Windows/Mac", "Laptop", "Android", "iPhone", "Tablet"],
    "Navegador": ["Chrome", "Firefox", "Edge", "Safari", "Opera"]
}

# Crear DataFrame con los índices
df = pd.DataFrame(matriz, columns=factores.keys())

# Mapear índices
for col, valores in factores.items():
    df[col] = df[col].apply(lambda x: valores[x])

# Resultados descriptivos
print(f"Total de combinaciones obtenidas: {len(df)}")
print(f"Cálculo: 4 x 5 x 3 x 5 x 5 = {4*5*3*5*5}")
print("\nPrimeros 15 casos de prueba :")
print(df.head(15))

# Guardar archivo completo
df.to_csv("matriz_completa_DOE.csv", index=False)
print("\n el archivo se genero correctamente: matriz_completa_DOE.csv")
