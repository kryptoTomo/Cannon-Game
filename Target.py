#!/usr/bin/python3

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import uniform
from utils import create_target

#############################################################

class Target(object):
    def __init__(self):
        self.pos = []
        self.hit = False
        self.counter=0

    def display_target(self):
        glScalef(0.8,0.8,0.8)
        if self.pos == []:
            self.pos = [0.0,0.4,0.0]
            self.pos[0], self.pos[2] = self.random_pos_target()
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        create_target()

    def counter_trigger(self):
        self.counter+=1
        print('Counter: ', self.counter)

    def random_pos_target(self):
        x = uniform(3.1,4.2)
        z = uniform(-1.2,1.2)
        return x, z

    def hit_target(self,x,y,z):
        tmp=False

        if(self.pos[0]-0.2625 <= x  and x <= self.pos[0]+0.2625):
            if(self.pos[1]-0.4 <= y  and y <= self.pos[1]+0.3):
                if(self.pos[2]-0.2625 <= z and z <= self.pos[2]+0.2625):
                    self.pos = []
                    tmp = True
                    self.counter_trigger()
        return tmp


    def keyboard_target(self,key):

        if key == b'1':
            self.pos[0] -= 0.2

        if key == b'2':
            self.pos[0] += 0.2

        if key == b'3':
            self.pos[2] -= 0.2

        if key == b'4':
            self.pos[2] += 0.2
