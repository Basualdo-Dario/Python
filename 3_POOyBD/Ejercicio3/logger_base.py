import logging as log

log.basicConfig(level = log.DEBUG ,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_data4.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__':

    log.debug('debug')

    log.info('info')

    log.warning('warning')

    log.error('error')

    log.critical('critical')
    
