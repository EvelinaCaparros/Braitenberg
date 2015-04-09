#!/usr/bin/env python

from math import sqrt
from Tkinter import *
from PIL import Image
from PIL import ImageTk

class Light:
    def __init__(self, master=0, x=0, y=0, intensity=1000):
        self._sizeX = 40
        self._sizeY = 40
        self._x = int(x)
        self._y = int(y)
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        self._intensity = float(intensity)
        self._master = master
        self._filename='light.png'
        image = Image.open(self._filename)
        image = image.resize((self._sizeX,self._sizeY), Image.ANTIALIAS)
        imagetk = ImageTk.PhotoImage(image)
        label = Label(master, image=imagetk)
        label.image = imagetk
        label.place(x=self._topX,y=self._topY)
        self._imagetk = imagetk
        self._container = label
    
    def getStrength(self, x, y):
        distance = sqrt( float((self._x - x)**2 +  (self._y - y)**2) )
        return self._intensity / distance

    def _update(self):
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        self._container.destroy()
        self._container = Label(self._master, image=self._imagetk)
        self._container.image = imagetk
        self._container.place(x=self._topX, y=self._topY)

    def getLocation(self):
        return self._x, self._y

    def move(self, x, y):
        self._x = x
        self._y = y
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
