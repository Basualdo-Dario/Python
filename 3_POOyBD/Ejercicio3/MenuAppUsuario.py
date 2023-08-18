from UsuarioDao import UsuarioDao as ud
from Ususario import Usuario as usu
from logger_base import log

opciones = None

while opciones != 5 :
    try:
        print('')
        print('1_Listar Usuarios')
        print('2_Agregar Usuario')
        print('3_Actualizar Usuario')
        print('4_Eliminar Usuario')
        print('5_Salir')
        opciones = int(input(''))

        if opciones == 1:
            registros = ud.seleccionar()
            for registro in registros:
                log.debug(registro)

        elif opciones == 2:
            username = input('Insertar username: ')
            password = input('Insertar passsword: ')
            usuarioI = usu(username=username,password=password)  
            ud.insertar(usuarioI)

        elif opciones == 3:
            id = int(input('Actualizar id: '))
            username = input('Actualizar username: ')
            password = input('Actualizar passsword: ')
            usuarioA = usu(id_usuario=id,username=username,password=password)
            ud.actualizar(usuarioA)

        elif opciones == 4:
            id = int(input('Eliminar id: '))
            usuarioE = usu(id_usuario=id)
            ud.eliminar(usuarioE)

        else:
            print('Adios.')
            
    except Exception as e:
        log.debug('Error: {e}')
        opciones = None