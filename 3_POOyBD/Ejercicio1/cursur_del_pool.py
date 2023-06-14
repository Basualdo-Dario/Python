from  logger_base import log    
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    

    def __exit__(self,tipo_execpion, valor_excepcion,detalle_excpcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'roolback,Ocurrio una execpcion: {valor_excepcion}, {tipo_execpion} ,{detalle_excpcion} ')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
       

if __name__ == '__main__':
    
    with CursorDelPool() as cursor:
        log.debug('dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())