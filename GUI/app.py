from model import Model
from view import View
from controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = App()

    model = Model()
    view = View(app)
    view.grid(row=0, column=0)

    controller = Controller(model, view)

    app.mainloop()
