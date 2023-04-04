from tkinter import *
from tkinter.messagebox import *


class LoginPage(object):
    def __init__(self, r=None):
        self.root = r  # r: Tk()
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='username: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='password: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='Login', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='Quit', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        from FirstPage import FirstPage
        name = self.username.get()
        secret = self.password.get()
        if name == '' and secret == '':
            self.page.destroy()
            FirstPage(self.root)
        else:
            showinfo(title='Oops!', message='Identification Failed！')
