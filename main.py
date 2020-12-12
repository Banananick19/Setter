import tkinter as tk
from common import *
from config import *

def main():
    root = tk.Tk()
    main_window = MainWindow(root)
    root.geometry('{}x{}'.format(size[0], size[1]))
    root.mainloop()

if __name__ == '__main__':
    main()


