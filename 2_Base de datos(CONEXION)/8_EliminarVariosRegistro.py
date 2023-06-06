import psycopg2

conexion = psycopg2.connect(user = 'postgres' ,password = 'admin',host = '127.0.0.1',port = '5432',database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia ='DELETE FROM persona WHERE id_persona IN  %s'
            valores = ((13,15,12),)
            cursor.execute(sentencia,valores)

            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)

except Exception as e:
    print(f'Error:{e}')
finally:
    conexion.close()


