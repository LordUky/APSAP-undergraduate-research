import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import askyesno


class FirstPage(object):
    def __init__(self, asts=None, rp=r"D:/ararat/data/files/N", r=None):

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

    def createPage(self):

        # Label(self.root, text='current root path: ', anchor='w').place(x=20, y=0, width=20, height=20)

        self.newPicButton = Button(self.root, text='Take New Picture', command=self.TakeNewPicture, state='disabled')
        self.newPicButton.place(x=20, y=180, width=200, height=20)

        Label(self.root, text='N:', anchor='w').place(x=20, y=30, width=20, height=20)

        self.combo1 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="readonly",
                               textvariable=self.combovar1)
        self.combo1.place(x=40, y=30, width=100, height=20)
        self.combo1.bind('<<ComboboxSelected>>', self.comcmd1)

        Label(self.root, text='Easting1:', anchor='w').place(x=20, y=60, width=100, height=20)
        self.combo2 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="disabled",
                               textvariable=self.combovar2)
        self.combo2.place(x=220, y=60, width=100, height=20)
        self.combo2.bind('<<ComboboxSelected>>', self.comcmd2)

        Label(self.root, text='Northing2:', anchor='w').place(x=20, y=90, width=100, height=20)
        self.combo3 = Combobox(self.root, values=[''] + self.pm.find_sub_dir(self.pm.root_path), state="disabled",
                               textvariable=self.combovar3)
        self.combo3.place(x=220, y=90, width=100, height=20)
        self.combo3.bind('<<ComboboxSelected>>', self.comcmd3)

        Label(self.root, text='Context Number:', anchor='w').place(x=20, y=120, width=200, height=20)
        self.combo4 = Combobox(self.root, values=['', 'create new'] + self.pm.find_sub_dir(self.pm.root_path),
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

        Label(self.root, text='Preview', bg='blue').place(x=500, y=60, width=480, height=360)

    def comcmd1(self, a=None):
        if self.combovar1.get() == '':
            return
        self.asts.fc['combo1'] = self.combovar1.get()
        self.pm.latitude = self.combovar1.get()
        self.combo2['state'] = 'readonly'
        self.combo2['values'] = self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}")
        return

    def comcmd2(self, a=None):
        if self.combovar2.get() == '':
            return
        self.asts.fc['combo2'] = self.combovar2.get()
        self.pm.num1 = self.combovar2.get()
        self.combo3['state'] = 'readonly'
        self.combo3['values'] = self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}")
        return

    def comcmd3(self, a=None):
        if self.combovar3.get() == '':
            return
        self.asts.fc['combo3'] = self.combovar3.get()
        self.pm.num2 = self.combovar3.get()
        self.combo4['state'] = 'readonly'
        self.combo4['values'] = ['create new'] + self.pm.find_sub_dir(
            f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")
        return

    def comcmd4(self, a=None):
        if self.combovar4.get() == '':
            self.newPicButton['state'] = 'disabled'
            return
        if self.combovar4.get() == 'create new':
            self.newPicButton['state'] = 'disabled'
            askback = askyesno('confirm', 'create new context??')
            if askback:
                self.NewContext()
            return
        else:
            self.asts.fc['combo4'] = self.combovar4.get()
        self.pm.context = self.combovar4.get()
        self.newPicButton['state'] = 'active'
        return

    def clear(self):
        for w in self.root.winfo_children():
            w.place_forget()

    def TakeNewPicture(self):
        from .SecondPage import SecondPage
        self.clear()
        SecondPage(self.asts, self.rootpath, self.root)

    def NewContext(self):
        if len(self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")) == 0:
            self.pm.create_context(1)
        else:
            self.pm.create_context(
                int(self.pm.find_sub_dir(f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")[-1]) + 1)
        self.combo4['values'] = ['create new'] + self.pm.find_sub_dir(
            f"{self.pm.root_path}/{self.pm.latitude}/{self.pm.num1}/{self.pm.num2}")

    def LogOut(self):
        self.root.destroy()
        # from .LoginPage import LoginPage
        # self.clear()
        # LoginPage(self.asts, self.root)
