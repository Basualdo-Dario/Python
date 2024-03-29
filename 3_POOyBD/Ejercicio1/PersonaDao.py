from logger_base import log
from Persona import Persona
from cursur_del_pool import CursorDelPool

class PersonaDao:
     
    '''
        DAO (data Access Object)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR=  'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR= 'UPDATE persona set nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
    _ELIMINAR= 'DELETE  FROM persona WHERE id_persona =%s'

    

    @classmethod
    def seleccionar(cls):
        with  CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)

            return personas

    @classmethod
    def insertar(cls,persona):
        with  CursorDelPool() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount
        

    @classmethod
    def actualizar(cls,persona):
       with  CursorDelPool() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with  CursorDelPool() as cursor:
                cursor.execute(cls._ELIMINAR,(persona.id_persona,))


if __name__ == '__main__':


        
    persona1 = Persona(nombre='Ruben',apellido='Forlan',email='RF@gmail.com')
    PersonaDao.insertar(persona1)

    persona1 = Persona(id_persona=28,nombre='Emanuel',apellido='Rojo',email='ER@gmail.com')
    PersonaDao.actualizar(persona1)

    persona1 = Persona(id_persona=27)
    PersonaDao.eliminar(persona1) 

    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona) 
        
    
    


