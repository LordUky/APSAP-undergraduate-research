from tkinter import *
from .LoginPage import *

class GUImain():

    def __init__(self, asts = None):
        root = Tk()
        root.title('APSAP')
        LoginPage(asts, root)
        root.mainloop()
        print("ML END")
        del(self.asts.sr)