#!/usr/bin/env python

from World import *
from Light import *
from Bot import *


def main():
    world = World()
    l = Light()
    l.move(2,2)
    world.addLight(l)
    b = Bot(4,4)
    print b.getLocation()
    b.process(world)
    print b.getLocation()
    print l.getLocation()
    print l.getLocation()
    print 'hi'


if __name__ == '__main__':
    main()
