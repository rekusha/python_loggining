import logging
import requests

logger = logging.getLogger()  # создаем объект логера
# .getLorreg() может принимать в качестве аргумента имя
# это единственный аргумент который она принимает.
# ЕСЛИ имя не передано то функция .getLogger создает корневой логер, объект класса RootLogger если его нет,
# а если он был уже где-то создан то возвращает этот объект уже созданный ранее
# ЕСЛИ имя было передано то логгер создает новый ИМЕНОВАННЫЙ логгер либо возвращает уже созданный
# поэтому логеры надо настраивать - об этом далее


print(logger)


def main(name):
    logger.warning(f'!1! Enter in the main() function: name = {name}')

    # loggining level (уровни логера)
    # NOTSET - 0
    # DEBUG - 10
    # INFO - 20
    # WARNING - 30
    # ERROR - 40
    # CRITICAL - 50

    logger.debug(f'!2! Enter in the main() function: name = {name}')  # уровень 10
    # не выдает сообщений потому как уровень логирования root уровня по умолчанию 30
    print('logger level ' + str(logger.level))

    # изменение уровня чувствительности уровня логера до DEBUG
    logger.setLevel('DEBUG')  # logging.DEBUG <- тоже можно
    # этот уровень определяет какие вообще сообщения будет передавать метод в свои обработчики
    # [<StreamHandler <stderr> (NOTSET)>]  <- обработчик, куда вытает сообщение и уровень логера

    print(logger.level)
    logger.debug(f'!3! Enter in the main() function: name = {name}')  # уровень 10
    # снова не видим сообщения потому как обработчики тоже имеют уровень которые так же надо указывать

    print()
    print("logger handlers list:")
    print(logger.handlers)  # <- показывает список обработчиков но если обработчики не сконфигурированы
    # то создается stream handler который пишет сообщения в stderr поток
    # логер создается но не закрепляется за объектом и поэтому может только выводить сообщения и ничего более

    logging.basicConfig(level='DEBUG')  # базовое конфигурирование логера с уровнем DEBUG
    logger.warning(f'!basicconf 1!  Enter in the main() function: name = {name}')
    logger.debug(f'!basicconf 2! Enter in the main() function: name = {name}')
    logger.info(f'!basicconf 3! Enter in the main() function: name = {name}')

    print()
    print("logger handlers list after basicConfig:")
    print(logger.handlers)

    logging.basicConfig(level='DEBUG', filename='1.log')  # <- сейчас ничего не покажет как и записи в файл потому как
    # не может .basicConfig быть указан дважды (вроде). если закомментировать верхний .basicConfig то увидим не
    # root обработчик а fileHandler отому как указали в basicConfig filename
    # [<FileHandler D:\1.log (NOTSET)>] <- обработчик, куда вытает сообщение и уровень логера

    print()
    print(logger.handlers)
    logger.warning(f'!basicconf 1!  Enter in the main() function: name = {name}')
    logger.debug(f'!basicconf 2! Enter in the main() function: name = {name}')
    logger.info(f'!basicconf 3! Enter in the main() function: name = {name}')
    print(logger.handlers)

    print()
    r = requests.get('https://www.google.com')
    # DEBUG:urllib3.connectionpool:https://www.google.com:443 "GET / HTTP/1.1" 200 None
    # после запроса видим сообзение из модуля реквестст обработчика urllib3.connectionpool
    # это произошло из-за того, что модуль logging глобальный модуль для всего проекта и basicConfig создает модули
    # для всех используемых нами логеров потому как все логеры предки root логера

    print()
    for key in logging.Logger.manager.loggerDict:  # <- получение списка всех имеющихся логеров
        # (logging.Logger.manager.loggerDict - это словарь у которого кключь является наименованием логера)
        print(key)
    # urllib3.util.retry
    # urllib3.util
    # urllib3
    # urllib3.connection
    # urllib3.response
    # urllib3.connectionpool
    # urllib3.poolmanager
    # requests
    # так как requests работает поверх библиотеки urllib3 мы видем столько логеров

    print()
    logging.getLogger('urllib3').setLevel('CRITICAL') # <- после urllib3 логер не будет давать логов уровня ниже CRITICAL
    r = requests.get('https://www.google.com')
    print(str(r.status_code) + ' status code оединения видим а логов нет')



if __name__ == '__main__':
    main('rekusha')
