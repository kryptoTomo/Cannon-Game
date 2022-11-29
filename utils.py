#!/usr/bin/python3

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import cv2

#############################################################

texture = None

#############################################################

def create_cube(texture,x,y,z):

    #top
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(-x, y, z)
    glTexCoord2f(1.0,0.0); glVertex3f(x, y, z)
    glTexCoord2f(1.0,1.0); glVertex3f(x, y, -z)
    glTexCoord2f(0.0,1.0); glVertex3f(-x, y, -z)
    glEnd()
    #front
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS);
    glTexCoord2f(0.0,0.0); glVertex3f(x, -y, z)
    glTexCoord2f(1.0,0.0); glVertex3f(x, y, z)
    glTexCoord2f(1.0,1.0); glVertex3f(-x, y, z)
    glTexCoord2f(0.0,1.0); glVertex3f(-x, -y, z)
    glEnd()
    #right
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS);
    glTexCoord2f(0.0,0.0); glVertex3f(x, y, -z)
    glTexCoord2f(1.0,0.0); glVertex3f(x, y, z)
    glTexCoord2f(1.0,1.0); glVertex3f(x, -y, z)
    glTexCoord2f(0.0,1.0); glVertex3f(x, -y, -z)
    glEnd()
    #left
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(-x, -y, z)
    glTexCoord2f(1.0,0.0); glVertex3f(-x, y, z)
    glTexCoord2f(1.0,1.0); glVertex3f(-x, y, -z)
    glTexCoord2f(0.0,1.0); glVertex3f(-x, -y, -z)
    glEnd()
	#bottom
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(x, -y, z)
    glTexCoord2f(1.0,0.0); glVertex3f(-x, -y, z)
    glTexCoord2f(1.0,1.0); glVertex3f(-x, -y, -z)
    glTexCoord2f(0.0,1.0); glVertex3f(x, -y, -z)
    glEnd()
	#back
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(x, y, -z)
    glTexCoord2f(1.0,0.0); glVertex3f(x, -y, -z)
    glTexCoord2f(1.0,1.0); glVertex3f(-x, -y, -z)
    glTexCoord2f(0.0,1.0); glVertex3f(-x, y, -z)
    glEnd()

    glFlush()

def create_barrel(quadric):

    glRotatef(180,0.0,1.0,0.0)
    glTranslatef(0.0,0.0,-0.30)
    glColor3f(-0.2, 0., 0.)
    glColorMaterial(GL_FRONT, GL_AMBIENT)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.2,0.0,0.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.3, 0.3, 0.3))
    gluCylinder(quadric, 0.15, 0.12, 1.0, 32, 32)
    gluSphere(quadric, 0.15, 32, 32)

def create_wheel_r(quadric):

    glColor3f(0.2276, 0.1216, 0.0157)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidTorus(0.07, 0.19, 40, 50)
    glRotatef(90,0.0,1.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)

def create_wheel_l(quadric):

    glColor3f(0.2276, 0.1216, 0.0157)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0,0.0,0.0,1))
    glutSolidTorus(0.07, 0.19, 40, 50)
    glRotatef(90,0.0,1.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)
    glRotatef(90,1.0,0.0,0.0)
    gluCylinder(quadric, 0.04, 0.04, 0.19, 32, 32)

def create_canonball(quadric):

    glScalef(0.05,0.05,0.05)
    glTranslatef(4.0, 0.25, 0.0)
    glColor3f(0.3, 0.3, 0.3)
    glColorMaterial(GL_FRONT, GL_AMBIENT)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.3,0.3,0.3))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (0.2, 0.2, 0.2))
    gluSphere(quadric, 2.0, 20, 20)

def create_target():

    global texture

    glEnable(GL_TEXTURE_2D)
    create_cube(texture[3],0.15,.15,0.15)
    glDisable(GL_TEXTURE_2D)

def load_texture_from_image(file_names):

    texture = glGenTextures(len(file_names))

    for i in range(len(file_names)):
        im = cv2.imread(file_names[i]);
        im=cv2.flip(im,0)
        im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        im=im.astype(np.float32)
        
        
        glBindTexture(GL_TEXTURE_2D, texture[i])
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, im.shape[0], im.shape[1], 0, GL_RGB, 
    GL_UNSIGNED_BYTE, im)

    return texture

def texture_init():

    global texture
    texture = load_texture_from_image(['texture/grass.png','texture/sea.jpg','texture/high_rusted_iron.png','texture/crate.jpg'])