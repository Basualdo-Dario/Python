from logger_base import log
from Conexion import Conexion

class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('dentro de enter')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def  __exit__(self,tipo,valor,detalle):
        log.debug('dentro de exit')
        if valor:
            self._conexion.rollback()
            log.debug(f'Roolback:{tipo},{valor},{detalle}')
        else:
            self._conexion.commit()
            log.debug('Commit')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)



if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('dentro del with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())
   