from tkinter import *
from tkinter.ttk import Combobox


class FirstPage(object):
    def __init__(self, r=None):

        self.root = r # r: Tk()
        self.root.geometry('%dx%d' % (1000, 600))
        self.root.minsize(1000, 600)

        self.createPage()

    def createPage(self):

        Label(self.root, text='N:', anchor='w').place(x=20, y=30, width=20, height=20)
        Combobox(self.root).place(x=40, y=30, width=100, height=20)

        Label(self.root, text='Easting1:', anchor='w').place(x=20, y=60, width=100, height=20)
        Combobox(self.root).place(x=220, y=60, width=100, height=20)

        Label(self.root, text='Northing2:', anchor='w').place(x=20, y=90, width=100, height=20)
        Combobox(self.root).place(x=220, y=90, width=100, height=20)

        Label(self.root, text='Context Number:', anchor='w').place(x=20, y=120, width=200, height=20)
        Combobox(self.root).place(x=220, y=120, width=100, height=20)

        Button(self.root, text='Take New Picture', command=self.TakeNewPicture).place(x=20, y=180, width=200, height=20)

        Button(self.root, text='New Context', command=self.NewContext).place(x=20, y=210, width=200, height=20)

        Button(self.root, text='Log Out', command=self.LogOut).place(x=500, y=20, width=80, height=20)

        Label(self.root, text='Preview', bg='blue').place(x=500, y=60, width=480, height=360)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def TakeNewPicture(self):
        from SecondPage import SecondPage
        self.clear()
        SecondPage(self.root)

    def NewContext(self):
        pass

    def LogOut(self):
        from LoginPage import LoginPage
        self.clear()
        LoginPage(self.root)
