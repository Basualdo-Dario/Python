

class Usuario:

    def __init__(self,id_usuario = None,username = None,password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self,id):
        self._id_usuario = id

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,name):
        self._username = name

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = password

    def __str__(self):
        return f'ID: {self._id_usuario} NOMBRE: {self._username} PASSWORD: {self._password}'
    
if __name__ == '__main__':

    usu1 = Usuario()
    print(usu1)

    usu1.id_usuario = 123
    usu1.password= 353524
    usu1.username = 'Dada rodriguez'

    print(usu1)

    usu2 = Usuario(13,'dario',123124125)
    print(usu2)