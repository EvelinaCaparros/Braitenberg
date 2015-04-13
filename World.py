#!/usr/bin/env python

class World:
    
    def __init__(self, xLow=0, xHigh=800, yLow=0, yHigh=600):
        self._bots = []
        self._lights = []
        self._xLow = xLow
        self._yLow = yLow
        self._xHigh = xHigh
        self._yHigh = yHigh

    def addBot(self, bot):
        self._bots.append(bot)

    def addLight(self, light):
        self._lights.append(light)
    
    def nextFrame(self):
        for bot in self._bots:
            bot.process(self)

    def getBots(self):
        return self._bots

    def getLights(self):
        return self._lights

    def getBounds(self):
        return self._xLow, self._xHigh, self._yLow, self._yHigh

