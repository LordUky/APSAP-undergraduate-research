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

        self.createPage()

        cpf = self.cc.capture_preview()
        logging.debug("cpf", cpf)
        if cpf:
            tkim = ImageTk.PhotoImage(file=cpf)
            self.previewLabel.image = tkim
            self.previewLabel["image"] = tkim

    def createPage(self):
        Button(self.root, text='Retake', command=self.retake).place(x=60, y=100, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview', bg='black', fg='white').place(x=500, y=60, width=480, height=360)

        self.previewLabel = Label(self.root)
        self.previewLabel.place(x=500, y=90, width=480, height=360)

        cbox = Combobox(self.root, textvariable=StringVar())
        cbox['values'] = ('Material',)
        cbox.current(0)
        cbox.place(x=40, y=300, width=100, height=20)

        Label(self.root, text='Weight: xxx g').place(x=60, y=500, width=100, height=20)

        Button(self.root, text='Save as individual int()', command=self.saveAsIndividualInt).place(x=600, y=550,
                                                                                                   width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.asts, self.rootpath, self.root)

    def retake(self):
        print('retake reached')

        cpf = self.cc.capture_preview()
        print('cpf in retake:', cpf)
        if cpf:
            tkim = ImageTk.PhotoImage(file=cpf)
            self.previewLabel["image"] = tkim
            self.previewLabel.image = tkim
        else:
            print("retake cap prev fail")

    def nextSide(self):
        from .FirstPage import FirstPage
        self.clear()
        ThirdPage(self.asts, self.rootpath, self.root)

    def saveAsIndividualInt(self):
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
        fp = fp_parent + "/photos/2.jpg"

        print(fp)

        while True:
            cc_ret = self.cc.capture_image_and_download(fp)
            if (cc_ret == None):
                break
            else:
                print("Error {}".format(cc_ret))
                print("Please check connection and focus and try again.")
                input("Press Enter after fixing error")

        FourthPage(fp_parent, asts=self.asts, rp=self.rootpath, r=self.root)
