import logging
'''
#--logger = logging.getLogger()  # если не передаем имя то объект создает корневой логер, тоесть объект класс RootLogger
# Создает новый или возвращает уже имеющийся созданный в другом месте
#-print(logger)
# <RootLogger root (WARNING)>
# возвращает объект класса RootLogger с именем root и уровнем WARNING.

app_logger = logging.getLogger('app_logger')
# создаем логер с именем app_logger
print(app_logger)
# возвращает объект кдасса Logger с именем app_logger и уровнем WARNING
print(app_logger.parent)
# видно что у app_logger имеет родителя RootLogger

utils_logger = logging.getLogger('app_logger.utils')
print(utils_logger)
# <Logger app_logger.utils (WARNING)>
print(utils_logger.parent)
# <Logger app_logger (WARNING)> <- оворит о том что предком у utils_logger является app_logger
# тоесть вся цепочка выглядит как root.app_logger.utils_logger
#
# тоесть не смотря на то, что создано всего 2 логера их на самом деле в цепочке 3 потому как есть еще корневой логер
# у всех трех логеров уровень WARNING. Это произошло потому, что по умолчанию они наследуют уровень родителя


def main():
    pass
'''
'______________________________________________________________________'
logging.basicConfig()  # без создания базовой конфигурации или конкретной конфигурации логеров обработчики не создаются
# если у логера нет обработчика то логер проверяет свой уровень с сообщением и если оно должно обрабатыватья
# но обработчика у логера нет, то он передает свое сообщение на обработку предку и далее проверку уровня сообщений
# не делают а просто обробатываю при наличии обработчика

app_logger = logging.getLogger('app_logger')  # 1 создаем логер app_logger

console_handler = logging.StreamHandler()  # 4 <- создаем обработчик StreamHandler
app_logger.addHandler(console_handler)  # 4 <- обавляем обработчик к логгеру app_handler
# 4 после этого увидим собщение в логе Hello world без доп информации
f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')  # 5 <- создаем объект форматера
# 5 форматируется старым свойством с атрибутами - атрибуты форматера в документации
console_handler.setFormatter(f)  # 5 <- подключаем форматер к обработчику
# 6 DEBUG - app_logger.utils - Hello world
# 6 DEBUG:app_logger.utils:Hello world
# 6 если не указать propagation = False  то мы увидем лог от обработчика этого и его родителя
# потому как сообщения уходят выше по цепочке
app_logger.propagate = False
# 6 DEBUG - app_logger.utils - Hello world
# 6 в этом случае получим только одну строку потому как свойства передачи сообщений было отключено

# в итоге сообщение создано младшим логером utils_logger но из-за отсутствия обработчика он передал сообщение родителю,
# родитель имея обработчик обработал сообщение и не передал его выше из-за отключенного свойства передачи

print(app_logger)
print('app_logger handlers', app_logger.handlers)  # 3 видим отсуствие обработчиков у апплоггера

print()
print('Root handlers', app_logger.parent.handlers)  # 3 видим отсуствие обработчиков у корневого логгера
print()

utils_logger = logging.getLogger('app_logger.utils') # 2 создаем логер utils наследуемый из app_logger
utils_logger.setLevel('DEBUG')
# utils_logger.propagate = False  # <- при установлении данного параметра в False
# передача сообщений верхним логерам отключается
print(utils_logger)
print('utils_logger handlers', utils_logger.handlers)  # 3 видим отсуствие обработчиков у ютилс логгера

# сообщения поднимаются вверх как пузырьки - этот процесс называется propagation
# если у логеров установить свойство propagate в False по передачу собщений можно отключить, по умолчанию оно True


def main():
    utils_logger.debug('Hello world')


if __name__ == '__main__':
    main()
