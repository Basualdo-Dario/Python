import logging as log 

log.basicConfig( level= log.DEBUG,
                format='%(asctime)s : %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                 log.FileHandler('control_usuario'),
                 log.StreamHandler()      
                ])


if __name__ == '__main__':
    log.debug('Mensaje a Nivel debug')
    log.info('Mensaje a Nivel info')
    log.warning('Mensaje a Nivel warning')
    log.error('Mensaje a Nivel error')
    log.critical('Mensaje a Nivel critical')
