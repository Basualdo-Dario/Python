import psycopg2

conexion = psycopg2.connect(user = 'postgres',password ='admin',host ='127.0.0.1',port = '5432',database='test_db')


try:
    with conexion:
        with conexion.cursor() as cursor :

            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
            valores = ('Roman','Riquelme','RR@gmail.com')
            cursor.execute(sentencia,valores)
           # conexion.commit()



            registros_insertados = cursor.rowcount
            print(registros_insertados)



            sentencia ='SELECT * FROM persona'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)



except Exception as e:
    print(f'Error{e}')

finally:
    conexion.close()



