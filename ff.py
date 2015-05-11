import types

from tkinter import *

class _Message(Frame):
    """Display a simple message."""

    def __init__(self, message, callback=None):
        super().__init__(Tk())
        self.pack()
        self.master.title("Message")
        self.button = Button(self, text="   OK   ", command=self.master.destroy)
        self.button.pack(side=BOTTOM)
        self.message = Label(self, text=message)
        self.message.pack(side=TOP)
        if callback:
            self.button["command"] = callback

class Game(Frame):
    """The main game class handler."""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.saved_games = []
        self.load_menu = None
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.master.title("Final Fantasy-like Python game")
        self.new_game = Button(self, text="New Game", command=self.load_new_game)
        self.new_game.pack(fill="x")
        self.load_game = Button(self, text="Continue", command=self.load_saved_game)
        self.load_game.pack(fill="x")
        self.quit_game = Button(self, text="Quit", command=self.master.destroy)
        self.quit_game.pack(fill="x")

    def toggle_buttons(self, status):
        for attr in dir(self):
            if isinstance(getattr(self, attr), Button):
                getattr(self, attr)["state"] = status

    def kill_load_menu(self):
        self.toggle_buttons(NORMAL)
        self.load_menu.master.destroy()
        self.load_menu = None

    def load_new_game(self):
        MainMenu(None)
        self.master.destroy()

    def load_saved_game(self):
        self.toggle_buttons(DISABLED)
        if not self.saved_games:
            self.load_menu = _Message("No saved games found", self.kill_load_menu)
            return
        self.load_menu = LoadGame(self)
        self.load_menu.master.protocol("WM_DELETE_WINDOW", self.kill_load_menu)
        self.load_menu.mainloop()

class LoadGame(Frame):
    """Menu to load a saved game."""

    def __init__(self, master):
        super().__init__(Tk())
        self.pack()
        self.master.title("Load game")
        for i, save in enumerate(master.saved_games):
            Button(self, text="Save #" + str(i).zfill(len(str(len(master.saved_games)))), command=save.load).pack(fill="x")

class MainMenu(Frame):
    """Main game menu."""

    def __init__(self, save):
        super().__init__(Tk())
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.master.title("Main menu")
        self.current_menu = None
        if save is None:
            save = Save()
        self.save = save
        self.buttons = types.SimpleNamespace()
        for name in ("Junction", "Items", "Magic", "Materia", "Equip", "Status",
                     "Order", "Change", "Limit", "Ship", "Cards", "Training", "Save"):
            button = Button(self, text=name, command=self.load_menu(name))
            button.pack(fill="x")
            setattr(self.buttons, name.lower(), button)
        self.pack()

    def load_menu(self, name):
        def loader():
            self.toggle_buttons(DISABLED)
            self.current_menu = globals()[name + "Menu"](self.save)
            self.current_menu.protocol("WM_DELETE_WINDOW", lambda: self.toggle_buttons(NORMAL))
            self.current_menu.pack()
        return loader

    def toggle_buttons(self, status):
        for attr in dir(self):
            if isinstance(getattr(self, attr), Button):
                getattr(self, attr)["state"] = status

class JunctionMenu(Frame):
    def __init__(self, save):
        super().__init__(Tk())

class ItemsMenu(Frame):
    def __init__(self, save):
        super().__init__(Tk())
















if __name__ == "__main__":
    Game(Tk()).mainloop()
