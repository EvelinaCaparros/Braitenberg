# Braitenberg Robots

This project contains a braitenberg simulator where the direction is user defined based on a matrix (the K matrix).

## Recent Changes
* Added Start/Stop button for simulation
* self._x and self._y in Boy.py refer to the center of the Bot instead of the topleft corner
* the Bot and Light class attach themselves to the canvas and move around

## TODO
* Bots.py
  * Implement process function that defines the movement of the bot per frame
  * Check for bounds and prevent bots from going outside of the world
* Window.py
  * Add input for the bot size

