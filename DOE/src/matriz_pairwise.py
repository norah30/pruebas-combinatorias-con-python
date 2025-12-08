# generacion de la matriz pairwise 

from allpairspy import AllPairs
import csv

# definir factores y niveles 
tipo_cliente = ["Nuevo", "Premium", "Vip", "Corporativo"]
metodo_pago = ["Débito", "Crédito", "PayPal", "Transferencia", "Contra entrega"]
tipo_envio = ["Recogida en Tienda", "A Domicilio", "Internacional"]
dispositivo = ["Windows/Mac", "Laptop", "Android", "iPhone", "Tablet"]
navegador = ["Chrome", "Firefox", "Edge", "Safari", "Opera"]

parametros = [
    tipo_cliente,
    metodo_pago,
    tipo_envio,
    dispositivo,
    navegador
]

# generacion de casos 
casos = list(AllPairs(parametros))

# resultados
print("Combinaciones generadas:", len(casos))

total = 4*5*3*5*5
reduccion = ((total - len(casos)) / total) * 100
print(f"Reduccion: {reduccion:.1f}%")

# imprimir casos
print("Casos de prueba generados:")
print()
for i, c in enumerate(casos, 1):
    print(f"  {i}. {c}")

# guardar archivo
print()
with open("matriz_pairwise.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Tipo_Cliente", "Metodo_Pago", "Tipo_Envio", 
                     "Dispositivo", "Navegador"])
    
    for caso in casos:
        writer.writerow(caso)

print("el archivo se guardo correctamente: matriz_pairwise.csv")  