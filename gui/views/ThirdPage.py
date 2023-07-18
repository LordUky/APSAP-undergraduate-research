import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FourthPage import *
from PIL import ImageTk

import logging


class ThirdPage(object):
    def __init__(self, asts=None, rp=r"D:/ararat/data/files/N", r=None):
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.rootpath = rp
        self.root = r

        self.alterButton = None
        self.confirmButton = None

        self.createPage()

        self.cc.start_lv()
        self.asts.cp = 3

        # cpf = self.cc.capture_preview()
        # logging.debug("cpf", cpf)
        # if cpf:
        #     tkim = ImageTk.PhotoImage(file=cpf)
        #     self.previewLabel.image = tkim
        #     self.previewLabel["image"] = tkim

    def createPage(self):
        self.alterButton = Button(self.root, text='Take pic and preview', command=self.take)
        self.alterButton.place(x=60, y=100, width=200, height=40)

        self.confirmButton = Button(self.root, text='save photos and start scaling', command=self.saveAsIndividualInt)
        self.confirmButton.place(x=600, y=500, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview', bg='black', fg='white').place(x=500, y=60, width=480, height=360)

        self.previewLabel = Label(self.root, name="preview_label")
        self.previewLabel.place(x=500, y=90, width=480, height=360)

        Label(self.root, text='Choose Material: ').place(x=60, y=300)

        self.cbox = Combobox(self.root, textvariable=StringVar())
        self.cbox['values'] = ['', 'pottery', 'bone', 'stone', 'pottery seive', 'bone seive', 'stone seive', 'spetial finds']
        self.cbox.current(0)
        self.cbox.place(x=160, y=300, width=100, height=20)
        # self.cbox.bind('<<ComboboxSelected>>', self.materialSelected)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.asts, self.rootpath, self.root)

    def take(self):
        self.cc.stop_lv()
        self.confirmButton.configure(state='normal')
        self.alterButton.configure(text='abort')
        self.alterButton.configure(command=self.abort)
        pv_fp = self.cc.capture_image_and_download()
        if pv_fp:
            tkim = ImageTk.PhotoImage(file=pv_fp)
            self.previewLabel["image"] = tkim
            self.previewLabel.image = tkim
        else:
            print("retake cap prev fail")

    def abort(self):
        self.cc.start_lv()
        self.confirmButton.configure(state='disabled')
        self.alterButton.configure(text='Take pic and preview')
        self.alterButton.configure(command=self.take)

    def saveAsIndividualInt(self):
        self.asts.cp = -1
        self.cc.stop_lv()
        self.clear()
        # if os.path.exists(f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/1"):
        #     # os.makedirs(f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/"+str(int(self.pm.find_sub_dir(self, f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")[-1])+1))
        #     dir_list = self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")
        #     new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(max([int(x) for x in dir_list])+1)
        #     print("new dir:", new_dir)
        #     os.makedirs(
        #         new_dir
        #     )
        # else:
        #     os.makedirs((f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/1"))

        dir_list = self.pm.find_sub_dir(
            f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")

        fp_parent = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(
            max([int(x) for x in dir_list]))
        fp = fp_parent + "/photos/2.cr3"

        print(fp)

        self.cc.copy_tmp_image_to_fp(fp)

        FourthPage(fp_parent, asts=self.asts, rp=self.rootpath, r=self.root)
