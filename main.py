import sqlite3

Connection = sqlite3.connect("data/movimientos.db")    #Indicamos la ruta donde esta la bd

#Establecer conexion
cur = Connection.cursor()                              #conectar a la base de datos

#Crear manejador de consutlas, llamado cursor
query = "   SELECT tipo_movimiento, concepto, fecha, cantidad, categoria from movimientos"

#Ejecutar la sentencia SQL en  la base de datos y recuperar los datos si loos hay en la variable res
res = cur.execute(query)

for fila in res:
    print(fila)                                         #Devuelve una tupla

