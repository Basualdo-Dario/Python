import psycopg2

conexion = psycopg2.connect(user = 'postgres',password = 'admin',host = '127.0.0.1',port = '5432',database = 'test_db')


try:
    with conexion:
        with  conexion.cursor() as cursor:


            sentencia ='SELECT nombre,apellido FROM persona WHERE id_persona IN %s'
            id = ((input('ID: '),input('ID: '),input('ID: ')),)

            cursor.execute(sentencia,id)
            registros = cursor.fetchall()

            for registro in registros:
                print(registro)


except Exception as e:
    print(f'error: {e}')

finally:
    conexion.close()

