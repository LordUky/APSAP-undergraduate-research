import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk  # ImageTk needs to be installed separately
from cam_ctrl import cam_ctrl
import time


class SecondPage(object):
    def __init__(self, asts, rp=r"D:/ararat/data/files/N", r=None):
        self.previewLabel = None
        self.pm = asts.pm
        self.asts = asts
        self.asts.cp = 2
        self.cc = asts.cc
        self.rootpath = rp
        self.root = r

        self.alterButton = None
        self.confirmButton = None

        self.createPage()


        # cpf = self.cc.capture_preview()
        # print("cpf", cpf)
        # if cpf:
        #     tkim = ImageTk.PhotoImage(file=cpf)
        #     self.previewLabel.image = tkim
        #     self.previewLabel["image"] = tkim
        # else:
        #     print("[ERROR]\tcapture preview fail")
        self.cc.start_lv()
        self.asts.cp = 2
        self.asts.pic_taken = False

    def createPage(self):
        self.alterButton = Button(self.root, text='Take pic and preview', command=self.take)
        self.alterButton.place(x=60, y=100, width=200, height=40)

        Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving).place(x=60, y=200, width=200, height=40)

        Label(self.root, text='Preview').place(x=500, y=30, width=480, height=360)

        self.previewLabel = Label(self.root, name="preview_label", text='Preview')
        self.previewLabel.place(x=500, y=90, width=480, height=360)

        self.confirmButton = Button(self.root, text='Next Side', command=self.confirm, state='disabled')
        self.confirmButton.place(x=600, y=500, width=200, height=40)

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.asts, self.rootpath, self.root)

    def take(self):
        # turn off live view
        self.cc.stop_lv()
        self.asts.pic_taken = True
        time.sleep(0.1)

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
        # turn on live view
        self.cc.start_lv()
        self.asts.pic_taken = False
        time.sleep(0.1)

        self.confirmButton.configure(state='disabled')
        self.alterButton.configure(text='Take pic and preview')
        self.alterButton.configure(command=self.take)

    def confirm(self):
        self.asts.cp = -1
        self.cc.stop_lv()

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
                            max([int(x) for x in dir_list])) + "/photos/2.cr3"):
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

        self.cc.copy_tmp_image_to_fp(new_dir + "/1.cr3")

        ThirdPage(self.asts, self.rootpath, self.root)
