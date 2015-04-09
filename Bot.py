#!/usr/bin/env python

from Light import *
from Tkinter import *
from math import sin,cos,radians
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
        self._oldAngle = self._angle


    def setMatrix(self, k11=1, k12=0, k21=0, k22=0):
        self._k11 = k11
        self._k12 = k12
        self._k21 = k21
        self._k22 = k22

    def _update(self):
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        if self._oldAngle != self._angle:
            image = Image.open(self._filename)
            image = image.resize((self._sizeX,self._sizeY), Image.ANTIALIAS)
            imagetk = ImageTk.PhotoImage(image.rotate(self._angle))
            self._container.destroy()
            self._container = Label(self._master, image=imagetk)
            self._container.image = imagetk
        self._container.place(x=self._topX, y=self._topY)
        self._oldAngle = self._angle

    def _rotate(self, xx, yy, cx, cy):

        angle = -self._angle

        # Center around origin
        x = xx - cx
        y = yy - cy

        # Use trig to rotate around origin
        newx = (x*cos(radians(angle))) - (y*sin(radians(angle)))
        newy = (x*sin(radians(angle))) + (y*cos(radians(angle)))

        # Translate back
        newx += cx
        newy += cy

        return newx,newy

    def process(self, world):
        # Cache values
        x = self._x
        y = self._y
        sizeX = self._sizeX
        sizeY = self._sizeY
        angle = self._angle

        # Find sensors
        sensorxL = x - (sizeX*3)/8
        sensoryL = y - sizeY/2
        sensorxR = x + (sizeX*3)/8 
        sensoryR = y - sizeY/2 

        # Rotate points by angle
        sensorxL,sensoryL = self._rotate(sensorxL, sensoryL, x, y)
        sensorxR,sensoryR = self._rotate(sensorxR, sensoryR, x, y)

        leftTotal = 0.0
        rightTotal = 0.0

        for light in world.getLights():
            leftTotal += light.getStrength(sensorxL, sensoryL)
            rightTotal += light.getStrength(sensorxR, sensoryR)

        """ At this point, sensorxL and sensoryL represents the location of 
            the left sensor and senxoryR and sensoryR is the location of
            the right sensor. We also have leftTotal and rightTotal which is
            the total amount of light that each sensor is detecting,
            respectively """

        # TODO: move this according to the k matrix and _stepDistance
        """ The end of this function needs to update the values of 
            self._x, self._y, and self._angle to whatever they should be
            and then call self._update to update the GUI """
        self._x += leftTotal + 10
        self._y += rightTotal + 10
        self._angle = 0

        self._update()

    def getLocation(self):
        return self._x, self._y

    def getAngle(self):
        return self._angle
