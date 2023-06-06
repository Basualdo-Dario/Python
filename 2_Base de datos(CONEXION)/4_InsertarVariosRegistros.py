import psycopg2

conexion = psycopg2.connect(user = 'postgres',password = 'admin',host = '127.0.0.1',port = '5432',database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
            valores =(
                ('Jorge','Rojas','JR@gmail.com'),
                ('Pedro','Mesa','PM@gmail.com'),
                ('Pequeña','Lulu','PL@gmail.com'),
                ('Bob','Esponja','BE@gmail.com'),
                ('Patricio','Estrella','PE@gmail.com')
                 )
            #executemany: sirve para insertar varios valores ala ves
            cursor.executemany(sentencia,valores)
            

            registro_insertado = cursor.rowcount
            print(registro_insertado)

            '''
            sentencia = 'DELETE FROM persona WHERE nombre = %s'
            valor = (('Roman'),)
            cursor.execute(sentencia,valor)
            '''

            sentencia ='SELECT * FROM persona'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)



except Exception as e:
    print(f'Error: {e}')
finally:
    conexion.close()