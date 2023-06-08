from tkinter import *
from .LoginPage import *

class GUImain():

    def __init__(self, pm = None):
        self.pm = pm
        root = Tk()
        root.title('APSAP')
        LoginPage(self.pm, root)
        root.mainloop()
