import tkinter
import PIL
from PIL import Image, ImageTk

class A: pass
a = A()

root = tkinter.Tk()
root.geometry("720x550")
cv = tkinter.Canvas(root, height=440, width=430)
cv.pack()

root.mainloop()

print("AA")
del(a)