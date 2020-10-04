# вместо словаря с настройками можно использовать формат .yml но это в доках описано полностью и принцип тот же что тут
import logging.config  # импорт модуля логгинг с конфигурированием
from _3settings import logger_config  # импорт словаря из файла


logging.config.dictConfig(logger_config)  # загрузка словаря с конфигом в логгер.конфиг
logger = logging.getLogger('app_logger')

# print(logger)  # 1 <Logger app_logger (WARNING)>  <- вся заеомментированное заменено инпортом из словаря конфигурации
#
# console_handler = logging.StreamHandler()
# logger.addHandler(console_handler)
#
# print(console_handler.level)  # 2 не получив сообзения в мэйн проверяем уровень обработчика - по умолчанию 0 (NOTSET)
# print(logger.level)  # 3 а у логгера уровень 30 и поэтому он не обрабатывает события меньше 30
#
# logger.setLevel('DEBUG')  # 4 устанавливаем уровень логгера в дебаг и видим  Enter in to the main() стандартный вывод
#
# # std_format = logging.Formatter(fmt='%(asctime)s-%(levelname)s-%(name)s-%(message)s')  # старый формат форматирование
# std_format = logging.Formatter(fmt='{asctime} - {levelname} - {name} - {message}', style='{')  # новое форматирование
# console_handler.setFormatter(std_format)  # подключаем форматтер к ОБРАБОТЧИКУ не логгеру и получаем на выходе
# # 2020-09-27 19:52:47,562 - DEBUG - app_logger - Enter in to the main()
# # дату время - уровень сообшения - имя логера - сообщение логера
#
# file_handler = logging.FileHandler('3.log', mode='a')  # создаем обработчик который будет писать ошибки в файл
# # mode = 'a' это указание на режим работы (по умолчанию a - append) - добавляет строки в конец файла
# logger.addHandler(file_handler)  # подключаем обработчик к логеру
# # без форматирования будем получать в файл стандартный ответ с сообщением "Enter in to the main()"
# # с флагом w - перезаписывает файл при добавлении логов
# file_handler.setFormatter(std_format)  # подключаем к ОБРАБОТЧИКУ форматтер и на выходе в файл имеем
# # 2020-09-27 20:17:55,535 - DEBUG - app_logger - Enter in to the main()


def main():
    logger.debug('Enter in to the main()')  # посе 1 ничего не выведет потому как нет обработчика


if __name__ == '__main__':
    main()
