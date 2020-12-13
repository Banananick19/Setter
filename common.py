from tkinter import *
from tkinter.filedialog import askopenfilenames
from config import *
import sys
from parserconfig import *
from GUI.widgets import *
from GUI.guimixin import *
from GUI.guimaker import GuiMakerFrameMenu


class Window(GuiMakerFrameMenu):

    def __init__(self, root):
        super().__init__(root)

    def make_widgets(self):
        pass

    def start(self):
        self.menu_bar = menu_bar


class ConfigMixin:

    def get_current_selection_name(self):
        pos = self.list_config_names.curselection()
        return self.list_config_names.get(first=pos)[0]

    def get_current_app_name(self):
        pos = self.list_apps.curselection()
        return self.list_apps.get(first=pos)[0]

    def get_append_to_index(self):
        pos = self.list_append_to_name.curselection()
        key = self.list_append_to_name.get(first=pos)[0]
        return len(self.config.configs[key]) + 1


    def validate_apps(self, apps, start=0):
        return dict((str(key), path) for key, path in enumerate(apps, start))


class MainWindow(Window, ConfigMixin):

    def __init__(self, root=None, config=Config()):
        self.config = config
        super().__init__(root)


    def delete_widgets(self):
        for e in self.main_frame.pack_slaves():
            e.destroy()

    def make_widgets(self):
        if not hasattr(self, 'main_frame'):
            self.main_frame = frame(self, bg='#f00')
        for config in self.config.configs:
            button(self.main_frame, side=TOP, text=config, command=lambda config=config: self.run_config(config))

    def run_config(self, config):
        errors = self.config.run_config(config)
        if errors:
            error_message = ''
            for key, message in errors.items():
                error_message += ERROR_FORMAT.format(key, message) + '\n'
            showerror(ERROR_BAD_PATH_MESSAGE, error_message)

    # START MAKE ADD ACTION

    def add_config(self):
        self.delete_widgets()
        self.new_config_name = StringVar('')
        self.new_apps = {}
        self.make_add_form()

    def make_add_form(self):
        entry(self.main_frame, side=TOP, linkvar=self.new_config_name)
        button(self.main_frame, side=TOP, text=APPS_CONFIG_LABEL,
               command=lambda: self.new_apps.update(self.validate_apps(askopenfilenames())))
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.new_config_action)

    def new_config_action(self):
        try:
            self.config.add_config(self.new_config_name.get(), self.new_apps)
        except:
            showerror(CONFIG_ALREADY_EXIST_ERROR, CONFIG_ALREADY_EXIST_ERROR_MESSAGE)
            return
        self.delete_widgets()
        self.make_widgets()

    # END MAKE ADD ACTION

    # START MAKE APPEND_TO ACTION

    def append_to_config(self):
        self.delete_widgets()
        self.new_apps = {}
        self.make_append_to_form()

    def make_append_to_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        button(self.main_frame, side=TOP, text=APPS_CONFIG_LABEL,
               command=lambda: self.new_apps.update(self.validate_apps(askopenfilenames(), self.get_append_to_index())))
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.append_to_config_action)

    def append_to_config_action(self):
        try:
            self.config.append_to_config(self.get_current_selection_name(), self.new_apps)
        except:
            showerror()
            return
        self.delete_widgets()
        self.make_widgets()

    # END MAKE APPEND_TO ACTION

    #START MAKE DELETE ACTION

    def delete_config(self):
        self.delete_widgets()
        self.make_delete_form()

    def make_delete_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.delete_config_action)

    def delete_config_action(self):
        try:
            self.config.delete_config(self.get_current_selection_name())
        except:
            showerror()
            return
        self.delete_widgets()
        self.make_widgets()

    # END MAKE APPEND_TO ACTION

    #START MAKE DELETE ACTION

    def reset_path_apps(self):
        self.delete_widgets()
        self.make_reset_path_apps_form()

    def on_select(self, e):
        self.config_name = self.get_current_selection_name()
        self.list_apps = listbox(self.main_frame,
                                     lines=self.config.configs[self.config_name].keys())
        self.list_apps.bind('<<ListboxSelect>>', self.on_select_app)

    def on_select_app(self, e):
        self.app_name = self.get_current_app_name()
        app_path = self.config.configs[self.config_name][self.app_name]
        self.current_path = askopenfilename(initialfile=app_path)

    def make_reset_path_apps_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        self.list_config_names.bind('<<ListboxSelect>>', self.on_select)
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.reset_path_apps_action)

    def reset_path_apps_action(self):
        try:
            self.config.reset_path(self.config_name, self.app_name, self.current_path)
        except:
            showerror()
            return
        self.delete_widgets()
        self.make_widgets()

    # END MAKE APPEND_TO ACTION