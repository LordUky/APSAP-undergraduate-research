from tkinter import *
from .LoginPage import *
from PIL import ImageTk


class GUImain():

    def __init__(self, asts=None):
        self.asts = asts
        self.root = Tk()
        self.root.title('APSAP')
        LoginPage(asts, self.root)

        self.root.after(100, self.refreshWeightHelper)
        self.root.after(100, self.refreshLvHelper)
        self.root.mainloop()
        print("ML END")
        del (self.asts.sr)
        self.asts.cc.stop_lv()

    def refreshLvHelper(self):
        if self.asts.cp == 2 or self.asts.cp == 3:
            try:
                img = self.asts.cc.get_lv_frame()
                img = ImageTk.PhotoImage(img)
                self.root.nametowidget("preview_label")["image"] = img
                self.root.nametowidget("preview_label").image = img
            except:
                pass
        self.root.after(100, self.refreshLvHelper)

    def refreshWeightHelper(self):
        if self.asts.cp == 4:
            self.root.nametowidget("weightLabel")['text'] = str(self.asts.sr.read())
        self.root.after(100, self.refreshWeightHelper)
