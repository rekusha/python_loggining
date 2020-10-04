import logging


class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        print(dir(record))  # распечатает словарь сохдаваемого объекта
        # print(record.rekusha_name) - так можно получить данные переданные из функции вызвавшей логгер с флагом extra
        # о надо помнить про то что у каждого экземпляра свой словарьи если вызвать как здесь то посыпятся ошибки
        # потому что у одного метода есть, а у другого нет ключа rekusha_name.
        return record.funcName == 'new_function'  # вернет тру в случае если в словаре объекта параметр record.funcName
        # имя функции откуда был выхван объект будет совпадать с 'new_function'


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filters': ['new_filter'],  # подключение фильтра
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    },

    'filters': {
        'new_filter': {
            '()': NewFunctionFilter,  # () говорит о создании объекта класса
            # : NewFunctionFilter - указывает путь с классу объект которого надо сохдать
            # если например фильтр был бы в файле filters.py то
            # сначало импорт
            # import filters
            # затем вместо NewFunctionFilter указать filters.NewFunctionFilter путь откуда берется этот класс
        }
    },
    # 'root': {},  # позволяет сконцфигурировать корневой логер. '': {} - означает корневой логер
    # 'incremental': True,  # - говорит о том что этот конфиг является дополнительным конфигом
}
