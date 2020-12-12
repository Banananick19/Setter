menu_bar = [
        ('Configs', 0,
            [('new_config',  0, 'self.add_config'),
             ('append_to_config',  0, 'self.append_to_config'),# lambda:0 is a no-op
             ('Quit',  0, 'sys.exit')]),       # use sys, no self here
        ]
size = [500, 500]
coords = ['center', 'center']


#encoding
ENCODING_FOR_CONFIG = 'utf-8'

#Messages

ERROR_BAD_PATH_MESSAGE = 'Неправильный путь файла.'
ERROR_FORMAT = 'Приложение: {}, не работает из-за ошибки: {}' # first is app name, second error_message

# FORM Labels

NAME_CONFIG_LABEL = 'Имя: '
APPS_CONFIG_LABEL = 'Приложения'
FORM_SUBMIT_LABEL = 'Создать'

#Form messages

SUCCESS_MESSAGE = 'Операция выполнена успешно'