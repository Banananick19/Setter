import os
import configparser
from config import *


class Config:

    def __init__(self, file_path='config.ini'):
        self.parser = configparser.ConfigParser()
        self.parser.read_file(open(file_path, encoding=ENCODING_FOR_CONFIG))
        self.configs = self.parser._sections
        self.config_file_path = file_path

    def save_changes(self):
        with open(self.config_file_path, 'w', encoding='utf-8') as configfile:
            self.parser.write(configfile)

    def add_config(self, config_name, config_apps):
        self.parser.add_section(config_name)

        for key, app in config_apps.items():
            self.parser.set(config_name, key, app)

        self.save_changes()

    def append_to_config(self, config_name, new_apps):
        apps = dict(self.parser[config_name])
        apps.update(new_apps)

        for key, app in apps.items():
            self.parser.set(config_name, key, app)

        self.save_changes()

    def delete_config(self, config_name):
        self.parser.remove_section(config_name)
        self.save_changes()

    def delete_app(self, config_name, app_name):
        self.parser.remove_option(config_name, app_name)
        self.save_changes()

    def rename_app(self, config_name, old_app, new_app):
        app_path = self.configs[config_name][old_app]
        self.parser.remove_option(config_name, old_app)
        self.parser.set(config_name, new_app, app_path)
        self.save_changes()

    def rename_config(self, old_config, new_config):
        apps = self.parser[old_config]
        self.parser[new_config] = apps
        self.save_changes()

    def reset_path(self, config_name, app_name, new_path):
        self.parser[config_name][app_name] = new_path
        self.save_changes()

    def run_config(self, config):
        config_apps = self.configs[config]
        errors = {}
        for key, app in config_apps.items():
            if os.path.exists(app) and os.path.isfile(app):
                os.popen(app)
            else:
                errors[key] = ERROR_BAD_PATH_MESSAGE
        return errors
