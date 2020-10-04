import logging.config
from _4settings import logger_config

logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')

words = ['new house', 'apple', 'ice cream', 3]


def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            # logger.debug(f'Exception here, item = {item}', exc_info=True)
            logger.exception(f'Exception here, item = {item}')
            pass


# при отлавливании исключений через блок try except, logger.debug() по умолчанию будет выдавать информацию, но из-за
# наличия блока except офибки не будут останавливать выполнение работы, для предотвращения этого используется параметр
# ecx_info=True или используется функция logger.exception()


if __name__ == '__main__':
    main()
