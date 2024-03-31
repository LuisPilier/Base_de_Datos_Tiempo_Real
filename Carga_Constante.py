import psycopg2
import random
import time

# Conexión a la base de datos
conn = psycopg2.connect(
    database="sistema_tiempo_real",
    user="postgres",
    password="Luiscarlosp1",
    host="localhost",
    port="5432",
)
cur = conn.cursor()

def prueba_carga_constante(num_iteraciones, tiempo_espera):
    for i in range(num_iteraciones):
        cur.execute("INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)",
                    (f"Usuario{i}", f"usuario{i}@ejemplo.com", f"contrasena{i}"))
        conn.commit()
        time.sleep(tiempo_espera)


prueba_carga_constante(1000, 0.1)
