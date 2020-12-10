import tkinter as tk
from tkinter import messagebox
from parserconfig import get_configs
from common import *
from config import *


class MainWindow(tk.Frame):

    def __init__(self, root=None):
        self.root = root
        tk.Frame.__init__(self, root)
        self.pack(expand=1, fill=tk.BOTH)
        self.configs = get_configs()
        self.makewidgets()

    def makewidgets(self):
        print(self.configs)
        for key in self.configs:
            tk.Button(self, text=key, command=(lambda config=self.configs[key]: self.run_config(config))).pack()

    def center(self):
        if self.root is not None:
            x = (self.root.winfo_screenwidth() - size[0]) / 2
            y = (self.root.winfo_screenheight() - size[1]) / 2
            self.root.geometry('{}x{}+{}+{}'.format(*[int(x) for x in [size[0], size[1], x, y]]))
        else:
            raise Exception('Attribyte root must be set for Tk')


    def run_config(self, config):
        print(config)
        errors = run_config(config)
        if errors:
            error_message = str()
            for app, error_code in errors:
                error_message += 'app: {} exit with code: {}'.format(app, error_code)
            messagebox.showerror('errors', error_message)

def main():
    root = tk.Tk()
    main_window = MainWindow(root)
    root.geometry('{}x{}'.format(size[0], size[1]))
    main_window.center()
    root.mainloop()

if __name__ == '__main__':
    main()


