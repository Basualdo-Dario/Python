from logger_base import log
from Ususario import Usuario
from CursorDelPool import CursorDelPool

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE from usuario WHERE id_usuario =%s'

    @classmethod
    def seleccionar(cls):
        with  CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios =[]
            for i in registros:
                usuario = Usuario(i[0],i[1],i[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Usuaria agregado: {usuario}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'actualizado')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR,(usuario.id_usuario,))

if __name__ == '__main__':

    usu0 = Usuario(username='Dario',password=128)
    UsuarioDao.insertar(usu0)

    usu1 = Usuario(id_usuario=3,username='Luis',password=353)
    UsuarioDao.actualizar(usu1)

    usu2 = Usuario(id_usuario=11)
    UsuarioDao.eliminar(usu2)

    usu4 = UsuarioDao.seleccionar()
    for persona in usu4:
        log.debug(persona)


