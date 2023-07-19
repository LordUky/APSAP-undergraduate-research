import os.path
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox
from scale_read.scale_read import scaleRead


class LoginPage(object):
    def __init__(self, asts=None, r=None):
        self.asts = asts
        self.asts.cp = 0
        self.pm = self.asts.pm
        self.root = r  # r: Tk()
        self.root.geometry('%dx%d' % (700, 400))  # 设置窗口大小
        self.username = StringVar(value='autophoto')
        self.password = StringVar(value='Armenia1')
        self.pathN = StringVar(value=r"./photo_folder/N")
        self.url = StringVar(value="https://j20200007.kotsf.com/asl/")
        self.portCombo = None
        self.page = Frame(self.root)  # 创建Frame
        self.page.configure(bg=self.asts.bgColor)
        self.page.pack()
        Label(self.page, bg=self.asts.bgColor).grid(row=0, stick=W)
        Label(self.page, bg=self.asts.bgColor, text='username: ').grid(row=1, stick=E, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=W)
        Label(self.page, bg=self.asts.bgColor, text='password: ').grid(row=2, stick=E, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=W)
        Label(self.page, bg=self.asts.bgColor, text='set port: ').grid(row=3, stick=E, pady=10)
        self.portComboVar = StringVar()
        self.portCombo = Combobox(self.page, values=['x'] + scaleRead.detect_ports(), textvariable=self.portComboVar, state='readonly')
        self.portCombo.grid(row=3, column=1, stick=W)
        self.portCombo.current(0)
        self.portCombo.bind('<<ComboboxSelected>>', self.portSelected)
        Label(self.page, bg=self.asts.bgColor, text='path: ').grid(row=4, stick=E, pady=10)
        Entry(self.page, textvariable=self.pathN).grid(row=4, column=1, stick=W, padx=120, ipadx=100)
        Label(self.page, bg=self.asts.bgColor, text='server url: ').grid(row=5, stick=E, pady=10)
        Entry(self.page, textvariable=self.url).grid(row=5, column=1, stick=W, padx=120, ipadx=100)
        self.checkButtonIntVar = IntVar()
        self.surpriseCheckButton = Checkbutton(self.page, text='surprise mode', variable=self.checkButtonIntVar, bg=self.asts.bgColor)
        self.surpriseCheckButton.grid(row=6, pady=10)
        Button(self.page, text='Login', command=self.loginCheck, bg='Azure').grid(row=7, stick=W, pady=10)
        Button(self.page, text='Quit', command=self.page.quit, bg='Azure').grid(row=7, column=1, stick=W)

    def portSelected(self, a=None):
        if self.asts.sr == None:
            com_port = self.portComboVar.get()
            self.asts.sr = scaleRead(com_port, debug=(com_port == "x"))
            print("scale reader inited", self.asts.sr)

    def loginCheck(self):
        from .FirstPage import FirstPage
        name = self.username.get()
        secure = self.password.get()
        self.asts.pm.root_path = self.pathN.get()
        self.asts.api.base_url = self.url.get()
        if not os.path.exists(self.asts.pm.root_path):
            showinfo(title='Oops!', message='path invalid!')
            return
        status = self.asts.api.login(name, secure)
        if status == 1:
            self.asts.surprise = bool(self.checkButtonIntVar.get())
            self.page.destroy()
            self.portSelected()
            FirstPage(self.asts, self.root)
        else:
            showinfo(title='Oops!', message='Login Failed!')
