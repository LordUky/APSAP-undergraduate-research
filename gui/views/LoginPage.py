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
        self.root.geometry('%dx%d' % (300, 220))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.portCombo = None
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='username: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='password: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Label(self.page, text='set port: ').grid(row=3, stick=W, pady=10)
        self.portComboVar = StringVar()
        self.portCombo = Combobox(self.page, values=['x'] + scaleRead.detect_ports(), textvariable=self.portComboVar, state='readonly')
        self.portCombo.grid(row=3, column=1, stick=E)
        self.portCombo.current(0)
        self.portCombo.bind('<<ComboboxSelected>>', self.portSelected)
        Button(self.page, text='Login', command=self.loginCheck).grid(row=4, stick=W, pady=10)
        Button(self.page, text='Quit', command=self.page.quit).grid(row=4, column=1, stick=E)

    def portSelected(self):
        com_port = self.portComboVar.get()
        self.asts.sr = scaleRead(com_port, debug=(com_port == "x"))

    def loginCheck(self):
        from .FirstPage import FirstPage
        name = self.username.get()
        secret = self.password.get()
        if name == '' and secret == '':
            self.page.destroy()
            FirstPage(self.asts, self.pm.root_path, self.root)
        else:
            showinfo(title='Oops!', message='Identification Failed!')