import logging.config
from _5settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def new_function():
    logger.debug(f'Enter in to the new_function()')


def main():
    name = 'rekusha'
    logger.debug(f'Enter in to the main()')
    logger.debug(f'Enter in to the main()', extra={'rekusha_name': name})  # так можно передать значения переменных
    # для обработки в фильтрах или еще где


if __name__ == '__main__':
    main()
    new_function()
