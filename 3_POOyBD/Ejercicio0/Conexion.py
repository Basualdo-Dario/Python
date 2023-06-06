from logger_base import log
import psycopg2 as db
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _PORT='5432'
    _HOST='127.0.0.1'
    _conexion= None
    _cursor=None



    @classmethod
    def obtenerConexion(cls):
        if  cls._conexion is None:
            try:
                cls._conexion = db.connect(user =cls._USERNAME,
                                           password=cls._PASSWORD,
                                           host= cls._HOST,
                                           port=cls._PORT,
                                           database=cls._DATABASE )
                
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener la conexion: {e}')
                #sys tiene una funcion para terminar por completo el programa
                sys.exit()
        else:
            return cls._conexion






    @classmethod
    def obtenerCursor(cls):
        if cls._cursor == None:
            try:
                    cls._cursor = cls.obtenerConexion().cursor() 
                    log.debug(f'se abrio perfectamente el cursor {cls._cursor}')
                    return cls._cursor

            except Exception as e:
                log.error('Ocurrio un error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor
            
            


if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    
    

