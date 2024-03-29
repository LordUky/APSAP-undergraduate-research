import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter.font as tkFont
from .FourthPage import *
from PIL import ImageTk, Image
import time

import logging


class ThirdPage(object):
    def __init__(self, asts=None, r=None):
        self.previewPicLabel = None
        self.previewLabel = None
        self.exitButton = None
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.root = r

        self.alterButton = None
        self.confirmButton = None

        self.createPage()

        self.colorMembers = [self.root, self.alterButton, self.confirmButton, self.exitButton, self.previewLabel, self.previewPicLabel]

        self.cc.start_lv()
        self.asts.cp = 3
        self.asts.pic_taken = False

        # cpf = self.cc.capture_preview()
        # logging.debug("cpf", cpf)
        # if cpf:
        #     tkim = ImageTk.PhotoImage(file=cpf)
        #     self.previewLabel.image = tkim
        #     self.previewLabel["image"] = tkim

    def createPage(self):

        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        Label(self.root, text='Page3/4 (photo2)', fg='white', bg='black', font=fontStyle).place(x=0,  y=550, width=400, height=50)

        self.alterButton = Button(self.root, text='Take pic and preview', command=self.take)
        self.alterButton.place(x=60, y=100, width=200, height=40)

        self.confirmButton = Button(self.root, text='save photos and start scaling', command=self.saveAsIndividualInt, state='disabled')
        self.confirmButton.place(x=600, y=500, width=200, height=40)

        self.exitButton = Button(self.root, text='Exit (Not Saving)', command=self.exitNotSaving, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.exitButton.place(x=60, y=200, width=200, height=40)

        self.previewPicLabel = Label(self.root, name="preview_label", text='Preview', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.previewPicLabel.place(x=500, y=90, width=480, height=360)

        self.previewLabel = Label(self.root, name="preview_label")
        self.previewLabel.place(x=500, y=90, width=480, height=360)


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
        FirstPage(self.asts, self.root)

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
            imgopen = Image.open(pv_fp).resize((480, 320))
            tkim = ImageTk.PhotoImage(imgopen)
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

        fp_parent = f"{self.pm.root_path}/{self.pm._latitude}/{self.pm._num1}/{self.pm._num2}/{self.pm.context}/finds/individual/{self.asts.api.get_max_find({'utm_hemisphere': 'N', 'utm_zone': self.pm.latitude, 'area_utm_easting_meters': self.pm.num1, 'area_utm_northing_meters': self.pm.num2, 'context_number': self.pm.context}) + 1}"
        fp = fp_parent + "/photos/2.cr3"

        self.cc.copy_tmp_image_to_fp(fp)

        FourthPage(fp_parent, asts=self.asts, r=self.root)
