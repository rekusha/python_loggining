import logging


class MegaHandler(logging.Handler):  # созздаем класс обработчика
    def __init__(self, filename):  # инициализируем его
        logging.Handler.__init__(self)  # основу через предков
        self.filename = filename  # свойство файлнэйм у класс и его значение

    def emit(self, record):  # этот метод есть в классе хэндлер но он не реализован и подразумевается что он
        # будет описан в классах наследниках (как у меня). получает на вход объект класса logrecord в качестве значения
        message = self.format(record)  # преобразовываем объект в строку
        # дальше описываем что именно делаем с полученной строкой (почта, телега, смс .....)
        with open(self.filename, 'a') as file:  # открываем файл
            file.write(message + '\n')  # записываем строку в файл
        # после описания класса его надо добавить в конфиг


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{',
        }
    },

    'handlers': {  # содержит в себе обработчики
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file': {  # добавляем обработчик с именем file
            '()': MegaHandler,  # при создании  "()" вызывает класс с путем MegaHandler
            'level': 'DEBUG',  # уровень обработчика
            'filename': '_6debug.log',  # передает в конструктор класса 'filename' c параметром '_6debug.log'
            'formatter': 'std_format'  # подключаем форматеровщик 'std_format'
        }
    },

    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']  # подключаем обработчик к логгеру
        }
    },

    # 'filters': {
    #     'new_filter': {
    #         '()': NewFunctionFilter,
    #     }
    # 'root': {},  # позволяет сконцфигурировать корневой логер. '': {} - означает корневой логер
    # 'incremental': True,  # - говорит о том что этот конфиг является дополнительным конфигом
}
