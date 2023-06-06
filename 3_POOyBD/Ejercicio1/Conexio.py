from logger_base import log 
import psycopg2 as db
import sys

class Conexion:
    _DATABASE ='test_db'   
    _USERNAME ='postgres'
    _PASSWORD ='admin'
    _PORT ='5432'
    _HOST ='127.0.0.1'
    _CONEXION = None
    _CURSOR = None


    @classmethod
    def obetenerConexion(cls):
        if cls._CONEXION == None:
            try:
                cls._CONEXION = db.connect(user = cls._USERNAME,
                                password = cls._PASSWORD,
                                host = cls._HOST,
                                port = cls._PORT,
                                database = cls._DATABASE )
                log.debug(f'Conexion exitosa: {cls._CONEXION}')
                return cls._CONEXION
            
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener la conexion: {e}')
                print (e)
                sys.exit()
        else:
            return cls._CONEXION
        
    @classmethod
    def obtenerCursor(cls):
        if cls._CURSOR  == None :
            try:

                cls._CURSOR = cls.obetenerConexion().cursor()
                log.debug(f'se abrio perfectamente el cursor {cls._CURSOR}')
                return cls._CURSOR
            
            except Exception as e:
                log.error('Ocurrio un error al obtener el cursor: {e}')
                sys.exit()    

        else:
            return cls._CURSOR


if __name__ == '__main__':
    Conexion.obetenerConexion()
    Conexion.obtenerCursor()
    
    