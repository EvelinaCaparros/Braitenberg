#!/usr/bin/env python

from Tkinter import *
from Bot import *
from Light import *
from World import *
from threading import Thread
from time import sleep

class Window:
    @staticmethod
    def _RGB(r, g, b):
        color = '#%02x%02x%02x' % (r, g, b)
        return color

    # Default values
    _menuWidth=200
    _menuHeight=600
    _menuColor = _RGB.__func__(240,240,240)
    _canvasColor = _RGB.__func__(218,218,218)
    _frequency = 20

    # Window constructor
    def __init__(self, w=800, h=600):
        self._root = Tk()
        self._root.title("Braitenberg Vehicles")
        self._root.resizable(width=FALSE, height=FALSE)
        self._canvas = Canvas(self._root,
                              width=w,
                              height=h,
                              bd=1,
                              relief=SUNKEN,
                              background=self._canvasColor,
                              )
        self._menu = Frame(self._root,
                           width=self._menuWidth,
                           height=self._menuHeight,
                           bd=1,
                           relief=SUNKEN,
                           bg=self._menuColor,
                           )
        self._canvas.grid(row=0, column=0, sticky=N+W, padx=2, pady=2)
        self._canvas.grid_propagate(False)
        self._menu.grid(row=0, column=1, sticky=N+W, padx=2, pady=2)
        self._menu.grid_propagate(False)
        self._k11 = StringVar()
        self._k12 = StringVar()
        self._k21 = StringVar()
        self._k22 = StringVar()
        self._bx = StringVar()
        self._by = StringVar()
        self._lx = StringVar()
        self._ly = StringVar()
        self._world = World()
        self._initMenu()
        self._isRunning = False

    # Place objects into window
    def _initMenu(self):
        self._menu.columnconfigure(0, weight=1)
        self._menu.columnconfigure(1, weight=1)
        stepButton = Button(self._menu, text="Step", command=self._step)
        quitButton = Button(self._menu, text="Quit", command=exit)
        simButton = Button(self._menu, text="Start Simulation", command=self._sim)
        self._simButton = simButton
        matrixLabel = Label(self._menu, text="K Matrix:")
        k11 = Entry(self._menu, justify=RIGHT, textvariable=self._k11)
        k12 = Entry(self._menu, justify=RIGHT, textvariable=self._k12)
        k21 = Entry(self._menu, justify=RIGHT, textvariable=self._k21)
        k22 = Entry(self._menu, justify=RIGHT, textvariable=self._k22)
        self._k11.set("1")
        self._k12.set("0")
        self._k21.set("0")
        self._k22.set("1")
        botPositionLabel = Label(self._menu, text="Position:")
        botXLabel = Label(self._menu, text="X:")
        botYLabel = Label(self._menu, text="Y:")
        bx = Entry(self._menu, justify=RIGHT, textvariable=self._bx)
        by = Entry(self._menu, justify=RIGHT, textvariable=self._by)
        self._bx.set("0")
        self._by.set("0")
        addBotButton = Button(self._menu, text="Add Bot", command=self._addBot)
        lightPositionLabel = Label(self._menu, text="Position:")
        lightXLabel = Label(self._menu, text="X:")
        lightYLabel = Label(self._menu, text="Y:")
        lx = Entry(self._menu, justify=RIGHT, textvariable=self._lx)
        ly = Entry(self._menu, justify=RIGHT, textvariable=self._ly)
        self._lx.set("0")
        self._ly.set("0")
        addLightButton = Button(self._menu, text="Add Light", command=self._addLight)

        # attach objects to menu in position
        stepButton.grid(row=0, column=0, sticky=N)
        quitButton.grid(row=0, column=1, sticky=N)
        simButton.grid(row=1, column=0, columnspan=2, sticky=N)
        matrixLabel.grid(row=2, column=0, columnspan=2, sticky=N)
        k11.grid(row=3, column=0, sticky=N)
        k12.grid(row=3, column=1, sticky=N)
        k21.grid(row=4, column=0, sticky=N)
        k22.grid(row=4, column=1, sticky=N)
        botPositionLabel.grid(row=5, column=0, columnspan=2, sticky=N)
        botXLabel.grid(row=6, column=0, sticky=N+E)
        botYLabel.grid(row=7, column=0, sticky=N+E)
        bx.grid(row=6, column=1, sticky=N)
        by.grid(row=7, column=1, sticky=N)
        addBotButton.grid(row=8, column=0, columnspan=2, sticky=N)
        lightPositionLabel.grid(row=9, column=0, columnspan=2, sticky=N)
        lightXLabel.grid(row=10, column=0, sticky=N+E)
        lightYLabel.grid(row=11, column=0, sticky=N+E)
        lx.grid(row=10, column=1, sticky=N)
        ly.grid(row=11, column=1, sticky=N)
        addLightButton.grid(row=12, column=0, columnspan=2, sticky=N)

    # displays the window
    def display(self):
        self._root.mainloop()

    def _step(self):
        self._world.nextFrame()

    def _run(self):
        while self._isRunning:
            self._world.nextFrame()
            sleep(1.0/self._frequency)

    def _sim(self):
        self._isRunning = not self._isRunning
        if self._isRunning:
            thread = Thread(target=self._run)
            thread.daemon = True
            thread.start()
            self._simButton["text"] = "Stop Simulation"
        else:
            self._simButton["text"] = "Start Simulation"

    def _addBot(self):
        b = Bot(self._canvas, self._bx.get(), self._by.get())
        k11 = self._k11.get()
        k12 = self._k12.get()
        k21 = self._k21.get()
        k22 = self._k22.get()
        b.setMatrix(k11,k12,k21,k22)
        self._world.addBot(b)

    def _addLight(self):
        l = Light(self._canvas, self._lx.get(), self._ly.get())
        self._world.addLight(l)

