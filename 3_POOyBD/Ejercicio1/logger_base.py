import logging as log 
""" 
    level= log.DEBUG       = indica el nivel de mensajes
    format='%(asctime)s:'  = dice que se va a ver la fecha
    %(levelname)s          = dice que  se va a ver el nivel del mensaje
    [%(filename)s]         = inidica que se va a ver el nombre del archivo que causa problemas
    %(lineno)s             = indica el numero de la linea del error
    %(message)s            = muestra el mensaje que he agregado

    
    datefmt='%I:%M:%S %P'  = es el formate que se va haber el tiempo

"""
log.basicConfig(level= log.DEBUG ,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers= [
                    log.FileHandler('capa_datos2.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__':

    log.debug('Mensaje a nivel Debug')

    log.info('Mensaje a nivel Info')

    log.warning('Mensaje a nivel warning')

    log.error('Mensaje a nivel error')

    log.critical('Mensaje a nivel critical')