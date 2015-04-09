#!/usr/bin/env python

from math import sqrt
from Tkinter import *

class Light:
    def __init__(self, master=0, x=0, y=0, intensity=100):
        self._x = int(x)
        self._y = int(y)
        self._intensity = float(intensity)
        self._master = master
        self._graphic = Button(master, text="Light")
        self._graphic.place(x=x,y=y)
    
    def getStrength(self, x, y):
        distance = sqrt( float((self._x - x)**2 +  (self._y - y)**2) )
        return self._intensity / distance

    def _update(self):
        self._graphic.place(x=self._x, y=self._y)

    def getLocation(self):
        return self._x, self._y

    def move(self, x, y):
        self._x = x
        self._y = y
