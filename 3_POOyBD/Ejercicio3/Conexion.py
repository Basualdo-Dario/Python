from psycopg2 import pool
from logger_base import log 
import sys

class Conexion:
    _DATABASE ='test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _PORT = '5432'
    _HOST= '127.0.0.1'
    _MINCON =1
    _MAXCON = 5
    _pool = None


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MINCON,cls._MAXCON,
                                              host = cls._HOST,
                                              user = cls._USERNAME,
                                              password = cls._PASSWORD,
                                              port = cls._PORT,
                                              database = cls._DATABASE)
                log.debug(f'Pool obtenido {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Error al obtener el pool{e}')
                sys.exit()
        else:
            return cls._pool
        

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida{conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexion liberada{conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Conexiones cerradas')




if __name__ =='__main__':
    conexion1 = Conexion.obtenerConexion()

    Conexion.liberarConexion(conexion1)


    conexion2 = Conexion.obtenerConexion()


    conexion3 = Conexion.obtenerConexion()

    conexion4 = Conexion.obtenerConexion()

    Conexion.liberarConexion(conexion3)

    conexion5 = Conexion.obtenerConexion()

    Conexion.liberarConexion(conexion4)

    conexion6 = Conexion.obtenerConexion()

    conexion7 = Conexion.obtenerConexion()

    conexion8 = Conexion.obtenerConexion()
  
    Conexion.cerrarConexiones()