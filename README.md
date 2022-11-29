# Cannon-Game
Project for a 3D Graphics Course/AGH WFiIS IS SEMESTER(VII)
====================

INFORMATION
-----------
Program tested using a virtual machine with Ubuntu 22.04.1 LTS.
Install Requirements: 

        sudo apt install python3.7
        sudo apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev
        sudo apt-get install libosmesa6
        export PYOPENGL_PLATFORM=osmesa
        pip install PyOpenGL
        pip install opencv-python
        pip install numpy

Cannon-Game
-----------------------
Launch the game by typing from the main program folder position

    python3 main.py

Game-Control
-----------------------
| Symbol    |   A description of the action
|-----------|--------------------------------------
| Keyboard  |
|   ' '     |     cannon shot
|   'w'     |     move the cannon forward
|   's'     |     move the cannon backwards
|   'a'     |     move the cannon to the left
|   'd'     |     move the cannon to the right
|   'q'     |     change the aim of the cannon up
|   'e'     |     change the aim of the cannon down
|   '1'     |     moves the target away
|   '2'     |     moves the target closer
|   '3'     |     move the cannon to the left
|   '4'     |     move the cannon to the right
|   Mouse   |     
|   'RC'    |     rotates the map to the right
|   'LC'    |     rotates the map to the left
|Scroll Down|     rotates the map down
|Scroll Up  |     rotates the map up
|   'MC'    |     reset configuration

Limitations
------------
You should shoot in the default camera setting, otherwise it incorrectly locates the target and a correctly made shot is not recorded.

