import psycopg2

#Creamos la conecxion
conexion = psycopg2.connect(
    user ='postgres',
    password='admin',
    host= '127.0.0.1',
    port='5432',
    database='test_db'
    )

#lo abrimos en un try o catch para poder cerrar la conecxion
try:

    with conexion:
        #creamos el cursor en un whit para que se cierre automaticamente.
        with conexion.cursor() as cursor:





            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)





            # el (%s)= placeholder  y es un parametro posicion significa  que hay que darle un valor 

            sentencia = 'SELECT id_persona,nombre FROM persona WHERE id_persona = %s'
            # creamos la variable para darle el valor
            id = 1
            # tambien la variable puede ser de tipo input osea que pide el valor al usuario

            id = input('valor id: ')


            # y lo pasamos y transformamos en tupla (id,) si es un solo valor para que sea tupla hay que ponerle coma al final
            cursor.execute(sentencia,(id,))

            # fetchone solo devuelve un valor
            registros = cursor.fetchone()
            print(registros)


except Exception as e:

    print(f'ocurrio un error: {e}')

finally:
    conexion.close()

