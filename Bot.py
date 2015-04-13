#!/usr/bin/env python

from Light import *
from Tkinter import *
from Preload import ImageCache
from math import sin,cos,atan,radians,degrees
from PIL import Image
from PIL import ImageTk

class Bot:
    
    _scale = .1

    def __init__(self, master=0, x=0, y=0, angle=0, sizeX=100, sizeY=100, sF = 1, k11=1.0, k12=0.0, k21=0.0, k22=1.0):
        self._sF = float(sF)
        
        self._sizeX = int(sizeX) * self._sF
        self._sizeY = int(sizeY) * self._sF
        
        self._sizeX = int(self._sizeX)
        self._sizeY = int(self._sizeY)
        
        self._x = int(x)
        self._y = int(y)
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        self._angle = int(angle)
        self._k11 = float(k11)
        self._k12 = float(k12)
        self._k21 = float(k21)
        self._k22 = float(k22)
        self._master = master
        self._cache = ImageCache(master, 'spider.png', self._sizeX, self._sizeY)
        self._cache[0].place(x=self._topX, y=self._topY)
        self._container = self._cache[0]
        self._oldAngle = self._angle


    def setMatrix(self, k11=1.0, k12=0.0, k21=0.0, k22=1.0):
        self._k11 = float(k11)
        self._k12 = float(k12)
        self._k21 = float(k21)
        self._k22 = float(k22)

    def _update(self):
        self._topX = self._x - self._sizeX/2
        self._topY = self._y - self._sizeY/2
        if self._oldAngle != self._angle:
            self._container.place_forget()
            self._container = self._cache[int(self._angle)%360]
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
        k11 = self._k11
        k12 = self._k12
        k21 = self._k21
        k22 = self._k22

        # Find sensors
        sensorxL_static = x - (sizeX*3)/8
        sensoryL_static = y - sizeY/2
        sensorxR_static = x + (sizeX*3)/8 
        sensoryR_static = y - sizeY/2 

        # Rotate points by angle
        sensorxL,sensoryL = self._rotate(sensorxL_static, sensoryL_static, x, y)
        sensorxR,sensoryR = self._rotate(sensorxR_static, sensoryR_static, x, y)

        s1 = 0.0
        s2 = 0.0

        for light in world.getLights():
            s1 += light.getStrength(sensorxL, sensoryL)
            s2 += light.getStrength(sensorxR, sensoryR)

        """ At this point, sensorxL and sensoryL represents the location of 
            the left sensor and senxoryR and sensoryR is the location of
            the right sensor. We also have s1 and s2 which are the total
            amount of light that each sensor is detecting, respectively """

        """ The end of this function needs to update the values of 
            self._x, self._y, and self._angle to whatever they should be
            and then call self._update to update the GUI """

        # Calculate as per k matrix
        w1 = k11 * s1 + k12 * s2
        w2 = k21 * s1 + k22 * s2

        # Scale values
        w1 *= self._scale
        w2 *= self._scale

        # Calculate resultant rotation
        rotation = degrees(atan((w2-w1)/(sensorxR_static-sensorxL_static)))

        # Update values
        self._angle = angle+rotation
        self._x,self._y = self._rotate(x,y-(w1+w2)/2, x, y)

        #resetting bounds
        xLow, xHigh, yLow, yHigh = world.getBounds()
        if self._x > xHigh+self._sizeX/2:
            self._x = xLow-self._sizeX/2

        elif self._x < xLow-self._sizeX/2:
            self._x = xHigh+self._sizeX/2

        if self._y > yHigh+self._sizeY/2:
            self._y = yLow-self._sizeY/2

        elif self._y < yLow-self._sizeY/2:
            self._y = yHigh+self._sizeY/2

        # Update GUI
        self._update()

    def getLocation(self):
        return self._x, self._y

    def getAngle(self):
        return self._angle
