import psycopg2 as bd

conexion = bd.connect(user='postgres',password ='admin',host='127.0.0.1',port='5432',database = 'test_db' )

try:
    with conexion:
        with conexion.cursor() as cursor:
    
            sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
            valores =('Chiquito','Romero','CR@gmailcom')
            cursor.execute(sentencia,valores)

            sentencia ='UPDATE persona SET nombre=%s WHERE id_persona=%s'
            valores = ('Marcos','22')
            cursor.execute(sentencia,valores)

    conexion.commit()

except Exception as e:
    print(f'No se realizo commit,Error: {e}')

finally:
    conexion.close()