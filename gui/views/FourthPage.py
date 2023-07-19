import tkinter, os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from .FirstPage import *
from PIL import ImageTk
import logging


class FourthPage(object):
    def __init__(self, fp_parent, asts=None, rp=r"D:/ararat/data/files/N", r=None):
        self.chooseMaterialLabel = None
        self.cbox = None
        self.weightLabel = None
        self.sampleButton = None
        self.sampleLabel = None
        self.materialLabel = None
        self.categoryLabel = None
        self.uploadButton = None
        self.pm = asts.pm
        self.asts = asts
        self.cc = asts.cc
        self.sr = asts.sr
        self.sr.start()
        self.rootpath = rp
        self.root = r
        self.fp_parent = fp_parent
        self.asts.cp = 4

        self.cboxVar = StringVar()
        self.material = ''
        self.category = ''
        self.weight = -1

        self.createPage()

        self.colorMembers = [self.root, self.sampleButton, self.sampleLabel, self.weightLabel, self.chooseMaterialLabel, self.uploadButton, self.materialLabel, self.categoryLabel]

    def createPage(self):
        self.sampleButton = Button(self.root, text='Sample', command=self.sample, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor(), activebackground='black', activeforeground='white')
        self.sampleButton.place(x=60, y=200, width=200, height=40)
        self.sampleLabel = Label(self.root, text='', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.sampleLabel.place(x=600, y=200, width=200, height=40)
        self.materialLabel = Label(self.root, text='', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.materialLabel.place(x=600, y=300, width=200, height=40)
        self.categoryLabel = Label(self.root, text='', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.categoryLabel.place(x=600, y=400, width=200, height=40)
        self.weightLabel = Label(self.root, text='', name="weightLabel", bg='black' if not self.asts.surprise else self.asts.getRandomColor(), fg="white" if not self.asts.surprise else self.asts.getRandomColor())
        self.weightLabel.place(x=300, y=200, width=200, height=40)
        self.uploadButton = Button(self.root, text='CONFIRM AND UPLOAD', command=self.confirmAndUplaod, bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor(), activebackground='blue', activeforeground='red', state='disabled')
        self.uploadButton.place(x=600, y=500, width=200, height=40)

        self.chooseMaterialLabel = Label(self.root, text='Choose Material: ', bg=self.asts.bgColor if not self.asts.surprise else self.asts.getRandomColor())
        self.chooseMaterialLabel.place(x=60, y=300)

        self.cbox = Combobox(self.root, textvariable=self.cboxVar)
        self.cbox['values'] = [(), ('pottery', 'body'), ('pottery', 'rim'), ('pottery', 'base'), ('pottery', 'handle'), ('pottery', 'spout'), ('metal', 'nail')]
        self.cbox.current(0)
        self.cbox.place(x=180, y=300, width=100, height=20)
        self.cbox.bind('<<ComboboxSelected>>', self.materialSelected)

    def materialSelected(self, a=None):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
        material_and_category = self.cboxVar.get().split()
        self.material = 'material='+material_and_category[0]
        self.category = 'category='+material_and_category[1]
        self.materialLabel['text'] = self.material
        self.categoryLabel['text'] = self.category

        self.checkAllSet()

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

    def sample(self):
        if self.asts.surprise:
            self.SurpriseColorUpdate()
            a = random.random()
            if a < 0.7:
                self.sampleButton.place(x=600 * random.random(), y=300 * random.random() + 200)
                return

        self.weight = self.sr.read()
        self.sampleLabel['text'] = 'sample='+str(self.weight)

        self.checkAllSet()

    def confirmAndUplaod(self):


        self.sr.stop()
        self.sr.write_to_file(self.weight, self.fp_parent + "/a.xlsx")


        oneDecimalWeight = float('{:.1f}'.format(self.weight))
        data = {
            'utm_hemisphere': 'N',
            'utm_zone': int(self.pm.latitude),
            'area_utm_easting_meters': int(self.pm.num1),
            'area_utm_northing_meters': int(self.pm.num2),
            'context_number': int(self.pm.context),
            'material': self.material,  # user input
            'category': self.category,  # user input
            'weight_grams': oneDecimalWeight,  # string/number with 1 decimal place
            'volume_millimeter_cubed': None  # put none at collecting stage
        }
        self.asts.api.create_find(data)

        FirstPage(self.asts, self.rootpath, self.root)

    def checkAllSet(self):
        if self.material == '' or self.category == '' or self.weight == -1:
            self.uploadButton.configure(state='disabled')
        else:
            self.uploadButton.configure(state='active')
