import tkinter as tk
import multiprocessing
import logging

from karen import app as karenapp

logging.basicConfig(level=logging.DEBUG)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.__ka = karenapp.App()
        self.__ka_process = None

    def create_widgets(self):
        self.button_start = tk.Button(self, text="Start", command=self.karen_run)
        self.button_start.pack(side="top")

        self.button_stop = tk.Button(self, text="Stop", command=self.karen_stop)
        self.button_stop['state'] = "disable"
        self.button_stop.pack(side="top")

        self.button_quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.button_quit.pack(side="top")

        self.label = tk.Label(self, text="(c) Karen v. " + karenapp.VERSION)
        self.label.pack(side="bottom")

    def karen_run(self):
        logging.debug("Karen started!")
        self.__ka_process = multiprocessing.Process(target=self.__ka.start)
        self.__ka_process.start()
        self.button_start['state'] = "disable"
        self.button_stop['state'] = "active"

    def karen_stop(self):
        logging.debug("Karen stopped!")
        self.__ka_process.terminate()
        self.button_start['state'] = "active"
        self.button_stop['state'] = "disable"


_window = tk.Tk()
_app = Application(master=_window)
_app.mainloop()