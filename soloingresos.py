import sqlite3

tipo = input("Ingreso o gasto (I//G): ").upper()

while tipo.upper() not in ("I", "G"):
    print("Elige un tipo existente")
    tipo = input("Ingreso o gasto (I//G): ")

#Establecer conexion
connection = sqlite3.connect("data/movimientos.db")

#Establecer conexion
cur = connection.cursor()                              #conectar a la base de datos

#Crear manejador de consutlas, llamado cursor
#query = f"SELECT tipo_movimiento, concepto, fecha, cantidad, categoria from movimientos WHERE tipo_movimiento = '{tipo}'" #MUY MALA PRACTICA. No usar comillas 

query = "SELECT tipo_movimiento, concepto, fecha, cantidad, categoria from movimientos WHERE tipo_movimiento = ? and cantidad > ?" #Los atributos deben ir en el execute

res = cur.execute(query, [tipo, 20])      #entre [] van los atributos de la consulta

#connection.commit()
#connection.close()

for fila in res:
    print(fila)