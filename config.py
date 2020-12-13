menu_bar = [
        ('Configs', 0,
            [('new_config',  0, 'self.add_config'),
             ('append_to_config',  0, 'self.append_to_config'),
             ('delete_config',  0, 'self.delete_config'),
             ('reset_path',  0, 'self.reset_path_apps'),# lambda:0 is a no-op
             ('Quit',  0, 'sys.exit')]),       # use sys, no self here
        ]
size = [500, 500]

MAIN_FRAME_COLOR = '#f00'

#encoding
ENCODING_FOR_CONFIG = 'utf-8'

#Messages
CONFIG_ALREADY_EXIST_ERROR = 'Already exists'
CONFIG_ALREADY_EXIST_ERROR_MESSAGE = 'Set with this name already exist'

CONFIG_APPEND_ERROR = 'Error'
CONFIG_APPEND_ERROR_MESSAGE = 'Can\'t add new app to set'

CONFIG_DELETE_CONFIG_ERROR = 'Error'
CONFIG_DELETE_CONFIG_ERROR_MESSAGE = 'Delete set wasn\'t finish success'

CONFIG_RESET_PATH_ERROR = 'Error'
CONFIG_RESET_PATH_ERROR_MESSAGE = 'Reset path for app was finish with error'

ERROR_BAD_PATH_MESSAGE = 'Bad app path.'
ERROR_FORMAT = 'App: {}, don\'t work: {}' # first is app name, second error_message

# FORM Labels

NAME_CONFIG_LABEL = 'Name: '
APPS_CONFIG_LABEL = 'Apps'
FORM_SUBMIT_LABEL = 'Submit'

#Form messages

SUCCESS_MESSAGE = 'success'