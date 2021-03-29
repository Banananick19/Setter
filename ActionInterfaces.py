from tkinter.filedialog import askopenfilenames, asksaveasfilename
from parserconfig import *
from GUI.widgets import *
from GUI.guimixin import *
from GUI.guimaker import GuiMakerFrameMenu
class ShortCutActionInterface:

    def make_shortcut(self):
        self.delete_widgets()
        self.make_make_shortcut_form()

    def make_make_shortcut_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.make_shortcut_action)

    def make_shortcut_action(self):

        self.config.make_shortcut(repr(self.get_current_selection_name()), asksaveasfilename(initialfile=self.get_current_selection_name() + '.py', filetypes=SHORTCUTS_TYPES))

        self.delete_widgets()
        self.make_widgets()

class AddConfigActionInterface:

    def add_config(self):
        self.delete_widgets()
        self.new_config_name = StringVar('')
        self.new_apps = {}
        self.make_new_config_form()

    def make_new_config_form(self):
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

class ResetPathActionInterface:

    def reset_path_apps(self):
        self.delete_widgets()
        self.make_reset_path_apps_form()

    def make_reset_path_apps_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        self.list_config_names.bind('<<ListboxSelect>>', self.on_select)
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.reset_path_apps_action)

    def reset_path_apps_action(self):
        try:
            self.config.reset_path(self.config_name, self.app_name, self.current_path)
        except:
            showerror(CONFIG_RESET_PATH_ERROR, CONFIG_RESET_PATH_ERROR_MESSAGE)
            return
        self.delete_widgets()
        self.make_widgets()


class AppendToConfigActionInteface:

    def append_to_config(self):
        self.delete_widgets()
        self.new_apps = {}
        self.make_append_to_config_form()

    def make_append_to_config_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        button(self.main_frame, side=TOP, text=APPS_CONFIG_LABEL,
               command=lambda: self.new_apps.update(self.validate_apps(askopenfilenames(), self.get_append_to_index())))
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.append_to_config_action)

    def append_to_config_action(self):
        try:
            self.config.append_to_config(self.get_current_selection_name(), self.new_apps)
        except:
            showerror(CONFIG_APPEND_ERROR, CONFIG_APPEND_ERROR_MESSAGE)
            return
        self.delete_widgets()
        self.make_widgets()

class DeleteConfigActionInterface:

    def delete_config(self):
        self.delete_widgets()
        self.make_delete_config_form()

    def make_delete_config_form(self):
        self.list_config_names = listbox(self.main_frame, lines=self.config.configs.keys())
        button(self.main_frame, side=TOP, text=FORM_SUBMIT_LABEL, command=self.delete_config_action)

    def delete_config_action(self):
        try:
            self.config.delete_config(self.get_current_selection_name())
        except:
            showerror(CONFIG_DELETE_CONFIG_ERROR, CONFIG_DELETE_CONFIG_ERROR_MESSAGE)
            return
        self.delete_widgets()
        self.make_widgets()