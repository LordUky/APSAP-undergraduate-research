import random
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font as tkFont
from tkinter.messagebox import askyesno
import os


class FirstPage(object):
    def __init__(self, asts=None, rp=r"D:/ararat/data/files/N", r=None):

        self.PreviewPicLabel = None
        self.ContextNumberLabel = None
        self.NorthingLabel = None
        self.EastingLabel = None
        self.NLabel = None
        self.newPicButton = None
        self.combo4 = None
        self.combo3 = None
        self.combo2 = None
        self.combo1 = None
        self.pm = asts.pm
        self.asts = asts
        self.asts.cp = 1
        self.rootpath = rp

        self.root = r  # r: Tk()
        self.root.geometry('%dx%d' % (1000, 600))

        self.combovar1 = tkinter.StringVar()
        self.combovar2 = tkinter.StringVar()
        self.combovar3 = tkinter.StringVar()
        self.combovar4 = tkinter.StringVar()

        self.createPage()

        self.colorMembers = [self.root, self.NLabel, self.EastingLabel, self.NorthingLabel, self.ContextNumberLabel, self.PreviewPicLabel]

    def createPage(self):

        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        Label(self.root, text='Page: 1 (config)', fg='white', bg='black', font=fontStyle).place(x=0,  y=550, width=400, height=50)

        # Label(self.root, text='current root path: ', anchor='w').place(x=20, y=0, width=20, height=20)
        if self.asts.surprise:
            self.root.configure(bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())

        self.newPicButton = Button(self.root, text='Take New Picture', command=self.TakeNewPicture, state='disabled')
        self.newPicButton.place(x=20, y=180, width=200, height=20)

        self.NLabel = Label(self.root, text='N:', anchor='w', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.NLabel.place(x=20, y=30, width=20, height=20)

        self.combo1 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="readonly",
                               textvariable=self.combovar1)
        self.combo1.place(x=40, y=30, width=100, height=20)
        self.combo1.bind('<<ComboboxSelected>>', self.comcmd1)

        self.EastingLabel = Label(self.root, text='Easting1:', anchor='w', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.EastingLabel.place(x=20, y=60, width=100, height=20)
        self.combo2 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="disabled",
                               textvariable=self.combovar2)
        self.combo2.place(x=220, y=60, width=100, height=20)
        self.combo2.bind('<<ComboboxSelected>>', self.comcmd2)

        self.NorthingLabel = Label(self.root, text='Northing2:', anchor='w', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.NorthingLabel.place(x=20, y=90, width=100, height=20)
        self.combo3 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="disabled",
                               textvariable=self.combovar3)
        self.combo3.place(x=220, y=90, width=100, height=20)
        self.combo3.bind('<<ComboboxSelected>>', self.comcmd3)

        self.ContextNumberLabel = Label(self.root, text='Context Number:', anchor='w', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.ContextNumberLabel.place(x=20, y=120, width=200, height=20)
        self.combo4 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path),
                               state="disabled", textvariable=self.combovar4)
        self.combo4.place(x=220, y=120, width=100, height=20)
        self.combo4.bind('<<ComboboxSelected>>', self.comcmd4)

        if self.asts.fc['combo1'] is not None:
            self.combo1.current(self.combo1['values'].index(self.asts.fc['combo1']))
            self.comcmd1()

        if self.asts.fc['combo2'] is not None:
            self.combo2.current(self.combo2['values'].index(self.asts.fc['combo2']))
            self.comcmd2()

        if self.asts.fc['combo3'] is not None:
            self.combo3.current(self.combo3['values'].index(self.asts.fc['combo3']))
            self.comcmd3()

        if self.asts.fc['combo4'] is not None:
            self.combo4.current(self.combo4['values'].index(self.asts.fc['combo4']))
            self.comcmd4()

        Button(self.root, text='Log Out', command=self.LogOut).place(x=500, y=20, width=80, height=20)

        self.PreviewPicLabel = Label(self.root, text='Preview', bg='blue')
        self.PreviewPicLabel.place(x=500, y=60, width=480, height=360)

    def comcmd1(self, a=None):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
        if self.combovar1.get() == '':
            return
        self.asts.fc['combo1'] = self.combovar1.get()
        self.pm.latitude = self.combovar1.get()
        self.combo2['state'] = 'readonly'
        self.combo2['values'] = self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}")
        return

    def comcmd2(self, a=None):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
        if self.combovar2.get() == '':
            return
        self.asts.fc['combo2'] = self.combovar2.get()
        self.pm.num1 = self.combovar2.get()
        self.combo3['state'] = 'readonly'
        self.combo3['values'] = self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}")
        return

    def comcmd3(self, a=None):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
        if self.combovar3.get() == '':
            return
        self.asts.fc['combo3'] = self.combovar3.get()
        self.pm.num2 = self.combovar3.get()
        self.combo4['state'] = 'readonly'
        # self.combo4['values'] = ['create new'] + self.pm.find_sub_dir(
        #     f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")
        self.combo4['values'] = self.asts.api.get_context_list({'utm_hemisphere': 'N', 'utm_zone': self.pm.latitude, 'area_utm_easting_meters': self.pm.num1, 'area_utm_northing_meters': self.pm.num2})
        print(self.combo4['values'], type(self.combo4['values']))
        return

    def comcmd4(self, a=None):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
        if self.combovar4.get() == '':
            self.newPicButton['state'] = 'disabled'
            return
        if False:
            pass
        # if self.combovar4.get() == 'create new':
        #     self.newPicButton['state'] = 'disabled'
        #     askback = askyesno('confirm', 'create new context??')
        #     if askback:
        #         self.NewContext()
        #     return
        else:
            self.asts.fc['combo4'] = self.combovar4.get()
        self.pm.context = self.combovar4.get()
        self.newPicButton['state'] = 'active'
        # print(os.listdir(os.path.curdir))
        # print(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}/{self.pm.context}")
        if not os.path.exists(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}/{self.pm.context}"):
            os.makedirs(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}/{self.pm.context}/finds/individual")
        return

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def TakeNewPicture(self):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
            a = random.random()
            if a < 0.6:
                self.newPicButton.place(x=100 * random.random(), y=300 * random.random() + 200)
                return
        from .SecondPage import SecondPage
        self.clear()
        SecondPage(self.asts, self.rootpath, self.root)

    # def NewContext(self):
    #     if self.asts.surprise:
    #         self.SurpriseColorUpdate()
    #     if len(self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")) == 0:
    #         self.pm.create_context(1)
    #     else:
    #         self.pm.create_context(
    #             int(self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")[-1]) + 1)
    #     self.combo4['values'] = ['create new'] + self.pm.find_sub_dir(
    #         f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")

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

    def LogOut(self):
        self.root.destroy()
        # from .LoginPage import LoginPage
        # self.clear()
        # LoginPage(self.asts, self.root)
