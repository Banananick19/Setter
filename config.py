menu_bar = [
        ('Configs', 0,
            [('new_config',  0, 'self.add_config'),
             ('append_to_config',  0, 'self.append_to_config'),
             ('delete_config',  0, 'self.delete_config'),
             ('reset_path',  0, 'self.reset_path_apps'),# lambda:0 is a no-op
             ('Quit',  0, 'sys.exit')]),       # use sys, no self here
        ]
size = [500, 500]
coords = ['center', 'center']


#encoding
ENCODING_FOR_CONFIG = 'utf-8'

#Messages
CONFIG_ALREADY_EXIST_ERROR = 'Уже существует'
CONFIG_ALREADY_EXIST_ERROR_MESSAGE = 'Конфиг с этим именем уже есть'

CONFIG_APPEND_ERROR = 'Ошибка'
CONFIG_APPEND_ERROR_MESSAGE = 'Не вышло добавить приложение в конфиг. Возмонжно ошибка пути файла.'

CONFIG_DELETE_CONFIG_ERROR = 'Ошибка'
CONFIG_DELETE_CONFIG_ERROR_MESSAGE = 'Не вышло удалить конфиг'

CONFIG_RESET_PATH_ERROR = 'Уже существует'
CONFIG_RESET_PATH_ERROR_MESSAGE = 'Не вышло сменить приложение'

ERROR_BAD_PATH_MESSAGE = 'Неправильный путь файла.'
ERROR_FORMAT = 'Приложение: {}, не работает из-за ошибки: {}' # first is app name, second error_message

# FORM Labels

NAME_CONFIG_LABEL = 'Имя: '
APPS_CONFIG_LABEL = 'Приложения'
FORM_SUBMIT_LABEL = 'Создать'

#Form messages

SUCCESS_MESSAGE = 'Операция выполнена успешно'