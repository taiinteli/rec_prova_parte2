# src/logging_config.py
import logging
import logging.handlers
import time

class LoggerSetup():

    def __init__(self):
        # instância do logger
        self.logger = logging.getLogger('')
        # configura o logger
        self.setup_logging()

    def setup_logging(self):
        # formata para o logger - utilizando a sintaxe de JSON
        LOG_FORMAT = '{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        # seta o nível do log para INFO.
        logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT)

        # adiciona o formatador ao logger
        formatter = logging.Formatter(LOG_FORMAT)

        # adiciona um handler para que os dados armazenados no logger também possam ser exibidos na tela
        console=logging.StreamHandler()
        # adiciona o formatador para o handler definido
        console.setFormatter(formatter)

        # guarda as info no arquivo
        log_file = "logs/app.log"
        # fonte: https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
        # o arquivo de log para ser rotacionado a cada 1 dia, (when=d + interval = 1 -> um dia) mantendo 10 arquivos anteriores.
        file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='d', interval=1, backupCount=10)
        file.setFormatter(formatter)

        # com os dois handlers criados, adicionamos eles ao logger
        self.logger.addHandler(console)
        self.logger.addHandler(file)



