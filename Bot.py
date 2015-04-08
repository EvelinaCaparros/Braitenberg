#!/usr/bin/env python

from Light import *

class Bot:
    
    _stepDistance = .01

    def __init__(self, x=0, y=0, angle=0, k11=1, k12=0, k21=0, k22=0):
        self._x = x
        self._y = y
        self._angle = angle
        self._k11 = k11
        self._k12 = k12
        self._k21 = k21
        self._k22 = k22

    def setMatrix(self, k11=1, k12=0, k21=0, k22=0):
        self._k11 = k11
        self._k12 = k12
        self._k21 = k21
        self._k22 = k22

    def process(self, world):
        # TODO: make these actual sensor locations
        sensorxL = self._x
        sensoryL = self._y
        sensorxR = self._x
        sensoryR = self._y

        leftTotal = 0
        rightTotal = 0

        for light in world.getLights():
            leftTotal += light.getStrength(sensorxL, sensoryL)
            rightTotal += light.getStrength(sensorxR, sensoryR)

        # TODO: move this according to the k matrix and _stepDistance
        self._x += leftTotal
        self._y += rightTotal

    def getLocation(self):
        return self._x, self._y

    def getAngle(self):
        return self._angle
