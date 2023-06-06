import psycopg2 as bd

conexion = bd.connect(user = 'postgres' ,password = 'admin',host = '127.0.0.1',port = '5432',database = 'test_db')

try:
    # esto es otra forma de hacerlo pero la mejor forma es con with
    
    conexion.autocommit = False

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores = ('Marco','Rojo','MR@gmail.com')
    cursor.execute(sentencia,valores)

    
    sentencia = 'UPDATE persona SET nombre=%s ,apellido=%s,email=%s  WHERE id_persona = %s'
    valores = ('Paulo','Dibala','PD@gmail.com','21')
    cursor.execute(sentencia,valores)


    conexion.commit()
    print('Se hizo commit,fin')

except Exception as e:
    # rollback() es volver atras 
    conexion.rollback()
    print(f'Se hizo roll Back,Error:{e}')
finally:
    conexion.close()


  