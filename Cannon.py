#!/usr/bin/python3

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin
import utils

#############################################################
class Cannon(object):
    def __init__(self):
        self.barrel = 0.0
        self.pos = [0.0,0.0,0.0]
        self.c_rot, self.c_move = 0.0, 0.0
        self.wr, self.wl = 0.0,0.0
        self.quadric = None
        self.quadric1 = None
        self.boom = 0

        self.di = 0
        self.t = 0.01
        self.hi = 0.0
        self.dc = 0.7
        self.v = 20
        self.g = 9.81
        self.velx = 0
        self.vely = 0
        self.pos_ball = [0.0,0.0,0.0]

    def display_cannon(self, quadric, target):

        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        glRotatef(self.c_rot,0.0,-1.0,0.0)

        glPushMatrix()
        glRotatef(self.barrel,1.0,0.0,0.0)
        utils.create_barrel(quadric)
        glPopMatrix()

        glPushMatrix()
        glRotatef(90,0.0,1.0,0.0)
        glTranslatef(0.0,-0.25,0.25)
        glRotatef(self.wr,0.0,0.0,1.0)
        utils.create_wheel_r(quadric)
        glPopMatrix()

        glPushMatrix()
        glRotatef(90,0.0,1.0,0.0)
        glTranslatef(0.0,-0.25,-0.25)
        glRotatef(self.wl,0.0,0.0,1.0)
        utils.create_wheel_l(quadric)
        glPopMatrix()

        glPushMatrix()
        self.display_canonball(quadric, self.barrel, target)
        glPopMatrix()

    def move_cannon(self, key, x, y):

        if key == b'q' and self.barrel < 90:
            self.barrel = (self.barrel + 0.5) % 360
        if key == b'e' and self.barrel > 0:
            self.barrel = (self.barrel - 0.5) % 360

        if key == b'w':
            tmp1 = self.pos[0] + sin(self.c_rot*3.1415/180)*0.08
            tmp2 = self.pos[2] - cos(self.c_rot*3.1415/180)*0.08
            if tmp1 > -4.8 and tmp1 < 4.8 and tmp2 > -2.2 and tmp2 < 2.2:
                self.pos[0] = tmp1
                self.pos[2] = tmp2
            self.wr = (self.wr + 7) % 360
            self.wl = (self.wl - 7) % 360

        if key == b's':
            tmp1 = self.pos[0] - sin(self.c_rot*3.1415/180)*0.08
            tmp2 = self.pos[2] + cos(self.c_rot*3.1415/180)*0.08
            if tmp1 > -4.8 and tmp1 < 4.8 and tmp2 > -2.2 and tmp2 < 2.2:
                self.pos[0] = tmp1
                self.pos[2] = tmp2
            self.wr = (self.wr - 7) % 360
            self.wl = (self.wl + 7) % 360

        if key == b'a':
            self.c_rot = (self.c_rot - 2) % 360
            self.wr = (self.wr + 7) % 360

        if key == b'd':
            self.c_rot = (self.c_rot + 2) % 360
            self.wl = (self.wl - 7) % 360

        self.fire(key)

        glutPostRedisplay()

    #############################################################

    def display_canonball(self, quadric, angle, target):

        if self.boom == 1:
            if self.di == 0.0 and self.hi == 0.0:
                self.velx = self.v*cos(angle*3.1415/180)
                self.vely = self.v*sin(angle*3.1415/180)

            glTranslatef(-0.2,self.hi,self.di)
            utils.create_canonball(quadric)

            a = [0]*16
            mat = list(glGetFloatv(GL_MODELVIEW_MATRIX,a))

            d = self.di - self.velx*self.t
            h = self.hi + (self.vely*self.t) - 1/2 * self.g * self.t ** 2

            self.di = d
            self.hi = h

            self.vely = self.vely - 9.8 * self.t

            if target.hit_target(mat[12],mat[13],mat[14]) or self.hi <-1.0:
                self.boom = 0
                self.hi = 0.0
                self.di = 0.0

        glutPostRedisplay();

    def fire(self, key):

        if key == b' ':
            self.boom = 1

        glutPostRedisplay()
