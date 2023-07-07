import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk
import pandas as pd
import logging


class FourthPage(object):
    def __init__(self, asts=None, rp=r"D:/ararat/data/files/N", r=None):
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.rootpath = rp
        self.root = r

        self.createPage()

    def createPage(self):
        Button(self.root, text='Sample', command=self.sample).place(x=60, y=200, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def sample(self):
        self.asts.scaleReader.initialize()
        weight = self.asts.scaleReader.read()
        self.asts.scaleReader.destroy()

        df = pd.DataFrame([weight])
        dir_list = self.pm.find_sub_dir(
            f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")

        path = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(
            max([int(x) for x in dir_list]))

        df.to_excel(path + "/a.xlsx", sheet_name='sheet1', index=False, header=False)

        self.clear()
        FirstPage(self.asts, self.rootpath, self.root)

