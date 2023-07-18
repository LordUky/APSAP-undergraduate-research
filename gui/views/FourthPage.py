import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk
import logging


class FourthPage(object):
    def __init__(self, fp_parent, asts=None, rp=r"D:/ararat/data/files/N", r=None):
        self.weightLabel = None
        self.sampleButton = None
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

        self.colorMembers = [self.root, self.sampleButton, self.weightLabel]

    def createPage(self):
        self.sampleButton = Button(self.root, text='Sample', command=self.sample, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor(), activebackground='black', activeforeground='white')
        self.sampleButton.place(x=60, y=200, width=200, height=40)
        self.weightLabel = Label(self.root, text='', name="weightLabel", bg='black' if not self.asts.surprise else self.asts.getRandomColor(), fg="white" if not self.asts.surprise else self.asts.getRandomColor())
        self.weightLabel.place(x=300, y=200, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def SurpriseColorUpdate(self):
        try:
            for i in self.colorMembers:
                try:
                    i.configure(bg=self.asts.getRandomColor())
                    i.configure(fg=self.asts.getRandomColor())
                except:
                    pass
        except:
            pass

    def sample(self):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
            a = random.random()
            if a < 0.7:
                self.sampleButton.place(x=600*random.random(), y=300*random.random() + 200)
                return

        weight = self.sr.read()
        self.sr.write_to_file(weight, self.fp_parent + "/a.xlsx")

        self.clear()
        self.sr.stop()
        FirstPage(self.asts, self.rootpath, self.root)
