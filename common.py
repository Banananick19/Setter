from tkinter import *
from config import *
from widgets import *
from parserconfig import *
from guimaker import GuiMakerFrameMenu


class Window(GuiMakerFrameMenu):

    def __init__(self, root):
        GuiMakerFrameMenu.__init__(self, root)

    def make_widgets(self):
        pass

    def start(self):
        self.menu_bar = menu_bar


class MainWindow(Window):

    def __init__(self, root=None, config=Config()):
        self.config = config
        Window.__init__(self, root)

    def delete_widgets(self):
        for e in self.main_frame.pack_slaves():
            e.destroy()

    def make_widgets(self):
        self.main_frame = frame(self, bg='#f00')
        for config in self.config.configs:
            button(self.main_frame, side=TOP, text=config, command=lambda config=config:self.config.run_config(config))

    def add_config(self):
        self.delete_widgets()


