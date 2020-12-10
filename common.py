import os
import sys

from config import *

def run_config(config_apps):
    errors = {}
    for key, app in config_apps.items():
        if os.path.exists(app) and os.path.isfile(app):
            os.popen(app)
        else:
            errors[key] = ERROR_BAD_PATH_MESSAGE
    return errors


