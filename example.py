#!/usr/bin/env python

from Tkinter import *
from PIL import Image
from PIL import ImageTk
import os, sys

dirlist = os.listdir('.')
print dirlist

dirlist = ['spider.png']
root = Tk()
for f in dirlist:
    try:
        image = Image.open('spider.png')
        photo = ImageTk.PhotoImage(image)

        label = Label(root,image=photo)
        label.image = photo
        label.pack()
    except Exception, e:
        pass

root.mainloop()

