import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *


class SecondPage(object):
    def __init__(self, pm = None, rp = r"D:\ararat\data\files\N", r=None):
        self.pm = pm
        self.rootpath = rp
        self.root = r
        self.createPage()

    def createPage(self):
        Button(self.root, text='Retake', command=self.retake).place(x=60, y=100, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview', bg='purple', fg='white').place(x=500, y=60, width=480, height=360)

        Button(self.root, text='Next Side', command=self.nextSide).place(x=600, y=500, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.pm, self.rootpath, self.root)

    def retake(self):
        pass

    def nextSide(self):
        from .ThirdPage import ThirdPage
        self.clear()
        ThirdPage(self.pm, self.rootpath, self.root)
