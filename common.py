from parserconfig import *
from GUI.widgets import *
from GUI.guimixin import *
from GUI.guimaker import GuiMakerFrameMenu
from ActionInterfaces import *


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
        return self.list_config_names.get(first=pos)

    def get_current_app_name(self):
        pos = self.list_apps.curselection()
        return self.list_apps.get(first=pos)

    def get_append_to_index(self):
        pos = self.list_config_names.curselection()
        key = self.list_config_names.get(first=pos)
        return len(self.config.configs[key]) + 1


    def validate_apps(self, apps, start=0):
        return dict((str(key), path) for key, path in enumerate(apps, start))


class MainWindow(Window, ConfigMixin, AddConfigActionInterface,
                 AppendToConfigActionInteface, DeleteConfigActionInterface, ResetPathActionInterface,
                 ShortCutActionInterface):

    def __init__(self, root=None, config=Config()):
        self.config = config
        super().__init__(root)


    def delete_widgets(self):
        for e in self.main_frame.pack_slaves():
            e.destroy()

    def make_widgets(self):
        if not hasattr(self, 'main_frame'):
            self.main_frame = frame(self, bg=MAIN_FRAME_COLOR)
        for config in self.config.configs:
            button(self.main_frame, side=TOP, text=config, command=lambda config=config: self.run_config(config))

    def run_config(self, config):
        errors = self.config.run_config(config)
        if errors:
            error_message = ''
            for key, message in errors.items():
                error_message += ERROR_FORMAT.format(key, message) + '\n'
            showerror(ERROR_BAD_PATH_MESSAGE, error_message)


    def on_select(self, e):
        self.config_name = self.get_current_selection_name()
        self.list_apps = listbox(self.main_frame,
                                     lines=self.config.configs[self.config_name].keys())
        self.list_apps.bind('<<ListboxSelect>>', self.on_select_app)

    def on_select_app(self, e):
        self.app_name = self.get_current_app_name()
        app_path = self.config.configs[self.config_name][self.app_name]
        self.current_path = askopenfilename(initialfile=app_path)
