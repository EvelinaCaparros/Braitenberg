#!/usr/bin/env python

from Light import *
from Tkinter import *
from math import sin,cos
from PIL import Image
from PIL import ImageTk

class Bot:
    
    _stepDistance = 1

    def __init__(self, master=0, x=0, y=0, angle=0, sizeX=100, sizeY=100, k11=1, k12=0, k21=0, k22=0):
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._x = int(x)
        self._y = int(y)
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        self._angle = int(angle)
        self._k11 = int(k11)
        self._k12 = int(k12)
        self._k21 = int(k21)
        self._k22 = int(k22)
        self._master = master
        self._filename='spider.png'
        image = Image.open(self._filename)
        image = image.resize((self._sizeX,self._sizeY), Image.ANTIALIAS)
        imagetk = ImageTk.PhotoImage(image.rotate(self._angle))
        label = Label(master, image=imagetk)
        label.image = imagetk
        label.place(x=self._topX,y=self._topY)
        self._container = label


    def setMatrix(self, k11=1, k12=0, k21=0, k22=0):
        self._k11 = k11
        self._k12 = k12
        self._k21 = k21
        self._k22 = k22

    def _update(self):
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        image = Image.open(self._filename)
        image = image.resize((self._sizeX,self._sizeY), Image.ANTIALIAS)
        imagetk = ImageTk.PhotoImage(image.rotate(self._angle))
        self._container.destroy()
        self._container = Label(self._master, image=imagetk)
        self._container.image = imagetk
        self._container.place(x=self._topX, y=self._topY)

    def process(self, world):
        # TODO: make these actual sensor locations
        sensorxL = self._x
        sensoryL = self._y
        sensorxR = self._x
        sensoryR = self._y

        leftTotal = 0.0
        rightTotal = 0.0

        for light in world.getLights():
            leftTotal += light.getStrength(sensorxL, sensoryL)
            rightTotal += light.getStrength(sensorxR, sensoryR)

        # TODO: move this according to the k matrix and _stepDistance
        self._x += leftTotal + 10
        self._y += rightTotal + 10

        self._update()

    def getLocation(self):
        return self._x, self._y

    def getAngle(self):
        return self._angle
