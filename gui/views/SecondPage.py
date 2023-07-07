import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk  # ImageTk needs to be installed separately
from cam_ctrl import cam_ctrl


class SecondPage(object):
    def __init__(self, asts, rp=r"D:/ararat/data/files/N", r=None):
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.rootpath = rp
        self.root = r

        self.createPage()

        cpf = self.cc.capture_preview()
        print("cpf", cpf)
        if cpf:
            tkim = ImageTk.PhotoImage(file=cpf)
            self.previewLabel.image = tkim
            self.previewLabel["image"] = tkim
        else:
            print("[ERROR]\tcapture preview fail")

    def createPage(self):
        Button(self.root, text='Retake', command=self.retake).place(x=60, y=100, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview').place(x=500, y=30, width=480, height=360)

        self.previewLabel = Label(self.root, text='Preview')
        self.previewLabel.place(x=500, y=90, width=480, height=360)

        Button(self.root, text='Next Side', command=self.nextSide).place(x=600, y=500, width=200, height=40)

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
        from .ThirdPage import ThirdPage
        self.clear()

        if os.path.exists(
                f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/1/photos"
        ):
            # new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(int(self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")[-1])+1)
            dir_list = self.pm.find_sub_dir(
                f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/")
            if os.path.exists(
                    f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(
                            max([int(x) for x in dir_list])) + "/photos/2.jpg"):
                new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(
                    max([int(x) for x in dir_list]) + 1) + "/photos"
                os.makedirs(new_dir)
            else:
                new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/" + str(
                    max([int(x) for x in dir_list])) + "/photos"

            print("2nd page new dir:", new_dir)

        else:
            new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/1/photos"
            os.makedirs(new_dir)

        while True:
            cc_ret = self.cc.capture_image_and_download(new_dir + "/1.jpg")
            if (cc_ret == None):
                break
            else:
                print("Error {}".format(cc_ret))
                print("Please check connection and focus and try again.")
                input("Press Enter after fixing error")

        ThirdPage(self.asts, self.rootpath, self.root)
