import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk
import logging


class FourthPage(object):
    def __init__(self, fp_parent, asts=None, rp=r"D:/ararat/data/files/N", r=None):
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.sr = asts.sr
        self.sr.start()
        self.rootpath = rp
        self.root = r
        self.fp_parent = fp_parent
        self.asts.cp = 4

        self.createPage()

        print(self.root.winfo_children())

    def createPage(self):
        Button(self.root, text='Sample', command=self.sample).place(x=60, y=200, width=200, height=40)
        Label(self.root, text='', name="weightLabel", bg='black', fg="white").place(x=300, y=200, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def sample(self):
        weight = self.sr.read()
        self.sr.write_to_file(weight, self.fp_parent + "/a.xlsx")

        self.clear()
        self.sr.stop()
        FirstPage(self.asts, self.rootpath, self.root)
