from logger_base import log

class Persona():

    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self,id):
        self._id_persona = id

    @property
    def nombre (self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,email):
        self._email = email

    def __str__(self):
        return f'''
        ID: {self._id_persona} , NOMBRE: {self._nombre} , APELLIDO: {self._apellido} , EMAIL: {self._email}'''
    



if __name__ == '__main__':
    per = Persona('1','Dario','Basualdo','DB@gmail.com')
    log.debug(per)

    pes = Persona(nombre='Luis',apellido='Basualdo',email='LB@gmail.com')
    log.debug(pes)