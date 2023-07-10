from tkinter import *
from .LoginPage import *

class GUImain():

    def __init__(self, asts = None):
        self.asts = asts
        self.root = Tk()
        self.root.title('APSAP')
        LoginPage(asts, self.root)

        self.root.after(100, self.refreshWeightHelper)
        self.root.mainloop()
        print("ML END")
        del(self.asts.sr)

    def refreshWeightHelper(self):
        if self.asts.cp == 4:
            self.root.nametowidget("weightLabel")['text'] = str(self.asts.sr.read())
        self.root.after(100, self.refreshWeightHelper)
