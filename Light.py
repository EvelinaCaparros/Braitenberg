#!/usr/bin/env python

from math import sqrt

class Light:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    
    def getStrength(self, x, y):
        distance = sqrt( (self._x - x)**2 +  (self._y - y)**2 )
        return 1 / (distance * distance)

    def getLocation(self):
        return self._x, self._y

    def move(self, x, y):
        self._x = x
        self._y = y
