import psycopg2

conecxion = psycopg2.connect(user = 'postgres',password = 'admin' , host = '127.0.0.1', port = '5432',database = 'test_db')

try:
    with conecxion:    
        with conecxion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valor = (('Rodrigo','Rodrigues','RR@gmail.com','14'),
                     ('Ricardo','Resorte','RR@gmail.com','12'),
                     ('Cristiano','Ronaldo','CR7@gmail.com','16'),
                     ('Leonel','Messi','LM@gmail.com','3'))
            cursor.executemany(sentencia,valor)

            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)


except Exception as e:
    print(f'Error: {e}')
finally:
    conecxion.close() 