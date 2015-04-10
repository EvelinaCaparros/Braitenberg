#!/usr/bin/env python

from Tkinter import *
from PIL import Image
from PIL import ImageTk
from threading import Thread

class ImageCache:

    def _load(self, master, filename, w, h): 
        for angle in range(1,361):
            image = Image.open(self._filename)
            image = image.resize((w,h), Image.ANTIALIAS)
            imagetk = ImageTk.PhotoImage(image.rotate(angle))
            label = Label(master, image=imagetk)
            label.image = imagetk
            self._images.append(label)
        self._loaded = True

    def __init__(self, master, filename, w, h):
        self._filename = filename
        self._images = []
        image = Image.open(self._filename)
        image = image.resize((w,h), Image.ANTIALIAS)
        imagetk = ImageTk.PhotoImage(image)
        label = Label(master, image=imagetk)
        label.image = imagetk
        self._images.append(label)
        self._loaded = False
        thread = Thread(target=self._load, args=(master, filename, w, h))
        thread.daemon = True
        thread.start()

    def __len__(self):
        while not self._loaded:
            pass
        return len(self._images)

    def __getitem__(self, i):
        ret = self._images[i]
        if ret:
            return ret    
        while not self._loaded:
            pass
        return self._images[i]
