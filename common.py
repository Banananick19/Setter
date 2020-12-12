from tkinter import *
from tkinter.filedialog import askopenfilenames
from config import *
from parserconfig import *
from GUI.widgets import *
from GUI.guimixin import *
from GUI.guimaker import GuiMakerFrameMenu


class Window(GuiMakerFrameMenu):

    def __init__(self, root):
        GuiMakerFrameMenu.__init__(self, root)

    def make_widgets(self):
        pass

    def start(self):
        self.menu_bar = menu_bar


class ValidatorMixin:

    def get_append_to_index(self):
        return len(self.config.configs[self.new_config_name.get()]) + 1


    def validate_apps(self, apps, start=0):
        return dict((str(key), path) for key, path in enumerate(apps, start))


class MainWindow(Window, ValidatorMixin):

    def __init__(self, root=None, config=Config()):
        self.config = config
        Window.__init__(self, root)

    def delete_widgets(self):
        for e in self.main_frame.pack_slaves():
            e.destroy()

    def make_widgets(self):
        self.main_frame = frame(self, bg='#f00')
        for config in self.config.configs:
            button(self.main_frame, side=TOP, text=config, command=lambda config=config: self.config.run_config(config))

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
        print(self.new_config_name, self.new_apps)
        self.config.add_config(self.new_config_name.get(), self.new_apps)
        self.delete_widgets()
        self.make_widgets()

    # END MAKE ADD ACTION

    # START MAKE APPEND_TO ACTION

    def append_to_config(self):
        self.delete_widgets()
        self.new_config_name = StringVar('')
        self.new_apps = {}
        self.make_append_to_form()

    def make_append_to_form(self):
        entry(self.main_frame, side=TOP, linkvar=self.new_config_name)
        button(self.main_frame, side=TOP, text=APPS_CONFIG_LABEL,
               command=lambda: self.new_apps.update(self.validate_apps(askopenfilenames(), self.get_append_to_index())))
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.append_to_config_action)

    def append_to_config_action(self):
        print(self.new_config_name, self.new_apps)
        self.config.append_to_config(self.new_config_name.get(), self.new_apps)
        self.delete_widgets()
        self.make_widgets()

    # END MAKE APPEND_TO ACTION
