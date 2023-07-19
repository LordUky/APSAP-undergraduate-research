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
        self.exitButton = None
        self.previewLabel = None
        self.previewPicLabel = None
        self.pm = asts.pm
        self.asts = asts
        self.asts.cp = 2
        self.cc = asts.cc
        self.rootpath = rp
        self.root = r

        self.alterButton = None
        self.confirmButton = None

        self.createPage()

        self.colorMembers = [self.root, self.alterButton, self.confirmButton, self.exitButton, self.previewLabel, self.previewPicLabel]

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
        self.alterButton = Button(self.root, text='Take pic and preview', command=self.take, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.alterButton.place(x=60, y=100, width=200, height=40)

        self.exitButton = Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.exitButton.place(x=60, y=200, width=200, height=40)

        self.previewLabel = Label(self.root, text='Preview', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.previewLabel.place(x=500, y=30, width=480, height=360)

        self.previewPicLabel = Label(self.root, name="preview_label", text='Preview', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.previewPicLabel.place(x=500, y=90, width=480, height=360)

        self.confirmButton = Button(self.root, text='Next Side', command=self.confirm, state='disabled', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.confirmButton.place(x=600, y=500, width=200, height=40)

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

    def exitNotSaving(self):
        self.clear()
        FirstPage(self.asts, self.rootpath, self.root)

    def take(self):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
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
            self.previewPicLabel["image"] = tkim
            self.previewPicLabel.image = tkim
        else:
            print("retake cap prev fail")

    def abort(self):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
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

        new_dir = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/{self.asts.api.get_max_find()+1}/photos"
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        self.cc.copy_tmp_image_to_fp(new_dir + "/1.cr3")

        ThirdPage(self.asts, self.rootpath, self.root)
