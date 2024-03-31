import psycopg2
import random
import threading
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

def prueba_concurrencia(num_hilos):
    def worker():
        while True:
            
            cur.execute("SELECT * FROM usuarios WHERE id = %s", (random.randint(1, 1000),))
            
            cur.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
                        (f"Producto{random.randint(1, 1000)}", random.randint(1, 100), random.randint(1, 10)))
            conn.commit()
            time.sleep(random.random())

    hilos = []
    for _ in range(num_hilos):
        hilo = threading.Thread(target=worker)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()


prueba_concurrencia(50)
