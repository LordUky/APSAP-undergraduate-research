import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from FirstPage import *


class ThirdPage(object):
    def __init__(self, r=None):
        self.root = r
        self.createPage()

    def createPage(self):
        Button(self.root, text='Retake', command=self.retake).place(x=60, y=100, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview', bg='black', fg='white').place(x=500, y=60, width=480, height=360)

        cbox = Combobox(self.root, textvariable=StringVar())
        cbox['values'] = ('Material', )
        cbox.current(0)
        cbox.place(x=40, y=300, width=100, height=20)

        Label(self.root, text='Weight: xxx g').place(x=60, y=500, width=100, height=20)

        Button(self.root, text='Save as individual int()', command=self.saveAsIndividualInt).place(x=600, y=550, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.root)

    def retake(self):
        pass

    def nextSide(self):
        from FirstPage import FirstPage
        self.clear()
        ThirdPage(self.root)

    def saveAsIndividualInt(self):
        pass
        self.clear()
        FirstPage(self.root)
