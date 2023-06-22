from logger_base import log
from psycopg2  import pool 
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _PORT='5432'
    _HOST='127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None



    @classmethod
    def obtenerpool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host = cls._HOST , 
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._PORT,
                                                      database = cls._DATABASE)
                
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerpool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion


    @classmethod
    def liberarConexion(cls,Conexion):
        #put = poner o colocar/ es decir que va a colocar el objeto conexion en el pool de conexiones
        cls.obtenerpool().putconn(Conexion)
        log.debug(f'Regresamos la conexion al pool: {Conexion}')


    @classmethod
    def CerrarConexiones(cls):
        #closeall() esto quiere decir que se van a cerrar todo los objetos de conexion
        cls.obtenerpool().closeall()


if __name__ == '__main__':
    conexion1  = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)

    conexion2  = Conexion.obtenerConexion()
    conexion3  = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    
    conexion4  = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion4)

    conexion5  = Conexion.obtenerConexion()     
  

