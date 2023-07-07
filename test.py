import tkinter
import PIL
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("720x550")
cv = tkinter.Canvas(root, height=440, width=430)

im = Image.open('test.jpg')
# im.show()
print(im)
tkim = ImageTk.PhotoImage(im)
cv.pack()
cv.create_image(0, 0, anchor='nw', image=tkim)

root.mainloop()
