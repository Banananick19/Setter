"""
###############################################################################
An extended Frame that makes window menus and toolbars automatically.
Use GuiMakerFrameMenu for embedded components (makes frame-based menus).
Use GuiMakerWindowMenu for top-level windows (makes Tk8.0 window menus).
See the self-test code (and PyEdit) for an example layout tree format.
###############################################################################
"""
from tkinter import *                     # widget classes
from tkinter.messagebox import showinfo


class GuiMaker(Frame):
    menu_bar = []                       # class defaults
    tool_bar = []                       # change per instance in subclasses
    helpButton = False                     # set these in start() if need self

    def __init__(self, root=None):
        Frame.__init__(self, root)
        self.root = root
        self.pack(expand=YES, fill=BOTH)        # make frame stretchable
        self.start()                            # for subclass: set menu/tool_bar
        self.make_menu_bar()                      # done here: build menu bar
        self.make_tool_bar()                      # done here: build toolbar
        self.make_widgets()                      # for subclass: add middle part

    def make_menu_bar(self):
        """
        make menu bar at the top (Tk8.0 menus below)
        expand=no, fill=x so same width on resize
        """

        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menu_bar:
            mbutton = Menubutton(menubar, text=name, underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.add_menu_items(pulldown, items)
            mbutton.config(menu=pulldown)

        if self.helpButton:
            Button(menubar, text    = 'Help',
                            cursor  = 'gumby',
                            relief  = FLAT,
                            command = self.help).pack(side=RIGHT)

    def add_menu_items(self, menu, items):
        for item in items:                     # scan nested items list
            if item == 'separator':            # string: add separator
                menu.add_separator({})
            elif type(item) == list:           # list: disabled item list
                for num in item:
                    menu.entryconfig(eval(num), state=DISABLED)
            elif type(item[2]) != list:
                menu.add_command(label     = item[0],         # command:
                                 underline = item[1],         # add command
                                 command   = eval(item[2]) if type(item[2]) == str else item[2])         # cmd=callable
            else:
                pullover = Menu(menu) 
                self.add_menu_items(pullover, item[2])          # sublist:
                menu.add_cascade(label     = item[0],         # make submenu
                                 underline = item[1],         # add cascade
                                 menu      = pullover)

    def make_tool_bar(self):
        """
        make button bar at bottom, if any
        expand=no, fill=x so same width on resize
        this could support images too: see Chapter 9,
        would need prebuilt gifs or PIL for thumbnails
        """
        if self.tool_bar:
            toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.tool_bar:
                Button(toolbar, text=name, command=action).pack(where)

    def make_widgets(self):
        pass

    def help(self):
        "override me in subclass"
        showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)

    def start(self): 
        "override me in subclass: set menu/toolbar with self"
        pass


###############################################################################
# Customize for Tk 8.0 main window menu bar, instead of a frame
###############################################################################

GuiMakerFrameMenu = GuiMaker           # use this for embedded component menus

class GuiMakerWindowMenu(GuiMaker):    # use this for top-level window menus
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        for (name, key, items) in self.menu_bar:
            pulldown = Menu(menubar)
            self.add_menu_items(pulldown, items)
            menubar.add_cascade(label=name, underline=key, menu=pulldown)

        if self.helpButton:
            if sys.platform[:3] == 'win':
                menubar.add_command(label='Help', command=self.help)
            else:
                pulldown = Menu(menubar)  # Linux needs real pull down
                pulldown.add_command(label='About', command=self.help)
                menubar.add_cascade(label='Help', menu=pulldown)


###############################################################################
# Self-test when file run standalone: 'python guimaker.py'
###############################################################################

if __name__ == '__main__':
    from guimixin import GuiMixin            # mix in a help method

    menu_bar = [
        ('File', 0,
            [('Open',  0, lambda:0),         # lambda:0 is a no-op
             ('Quit',  0, sys.exit)]),       # use sys, no self here
        ('Edit', 0,
            [('Cut',   0, lambda:0),
             ('Paste', 0, lambda:0)]) ]
    tool_bar = [('Quit', sys.exit, {'side': LEFT})]

    class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
        def start(self):
            self.menu_bar = menu_bar
            self.tool_bar = tool_bar

    class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
        def start(self):
            self.menu_bar = menu_bar
            self.tool_bar = tool_bar

    class TestAppWindowMenuBasic(GuiMakerWindowMenu):
        def start(self):
            self.menu_bar = menu_bar
            self.tool_bar = tool_bar    # guimaker help, not guimixin

    root = Tk()
    TestAppFrameMenu(Toplevel())
    TestAppWindowMenu(Toplevel())
    TestAppWindowMenuBasic(root)
    root.mainloop()
