import psycopg2

conexion = psycopg2.connect(user = 'postgres',password='admin',host='127.0.0.1',port= '5432',database ='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia='UPDATE persona SET nombre=%s,apellido=%s , email=%s WHERE id_persona=%s'
            valor = ('Calamardo','Tentaculos','CT@gmail.com',3)
            cursor.execute(sentencia,valor)



            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registro = cursor.fetchall()
            print(registro)

except Exception as e:
    print(f'Error{e}')
finally:
    conexion.close()

    