#!/usr/bin/python3

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Cannon
import Target
import utils


class CannonGame(object):
    def __init__(self):
        self.cx,self.cy,self.cz = 0.0, 0.0, 0.0
        self.ox,self.oy,self.oz = 0.0, 0.0, 0.0
        self.px,self.py,self.pz = -3.0, 3.0, 0.0

        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

        glutCreateWindow('Cannon game')
        glutReshapeWindow(1080,720)

        glutReshapeFunc(self.reshape) #définit la fonction de scène
        glutDisplayFunc(self.display)#définit la fonction d'affichage
        glutKeyboardFunc(self.keyboard) #définit la fonction des prises de commande par clavier
        glutMouseFunc(self.mouseControl)

        glClearColor (0.0, 0.0, 0.0, 0.0)
        glShadeModel (GL_SMOOTH)
        self.quadric = gluNewQuadric()
        gluQuadricDrawStyle(self.quadric, GLU_FILL)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.7, 0.7, 0.7, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.2, 0.2, 0.2, 1))
        glLightfv(GL_LIGHT0, GL_POSITION, (-1.0, 1.0, 1.0, 0.0))

        glEnable(GL_COLOR_MATERIAL)
        utils.texture_init()
        
        glEnable(GL_DEPTH_TEST)

        self.cannon = Cannon.Cannon()
        self.target = Target.Target()

    def RunGame(self):
        glutMainLoop()

    def reshape(self,width, height):

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        gluLookAt(-2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glMatrixMode(GL_MODELVIEW)

    def display(self):

        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(0.75,0.75,0.75)
        glLoadIdentity()
        
        glTranslatef(1.5,0.0,0.0)
        glRotatef(self.oy, 0.0, 1.0, 0.0)
        glTranslatef(-1.5,0.0,0.0)

        glTranslatef(1.5,0.0,0.0)
        glRotatef(self.oz, 0.0, 0.0, 1.0)
        glTranslatef(-1.5,0.0,0.0)
    
        ############################## pole armaty
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        # glTranslatef(6.0, 0.0, 0.0) 
        utils.create_cube(utils.texture[0],0.5,0.15,1)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        ############################## END

        ############################## water
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(1.5, 0.0, 0.0) 
        utils.create_cube(utils.texture[1],1,.1,1)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        ############################## END

        ############################## water
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glTranslatef(3, 0.0, 0.0) 
        utils.create_cube(utils.texture[2],0.5,.15,1)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        ############################## END
        glPushMatrix()
        self.target.display_target()
        glPopMatrix()

        glPushMatrix()

        glScalef(0.2,0.2,0.2)
        glTranslatef(0.0, 1.3, 0.0)
        glRotatef(90,0.0,-1.0,0.0) 
        self.cannon.display_cannon(self.quadric,self.target)

        glPopMatrix()

        glutSwapBuffers()


    def keyboard(self,key, x, y):

        self.cannon.move_cannon(key, x, y)
        self.target.keyboard_target(key)

        glutPostRedisplay()

    def mouseControl(self,key,b,c,d):
        #platform left
        if key == 0:
            self.oy = (self.oy - 10) % 360
        #platform right
        elif key == 2:
            self.oy = (self.oy + 10) % 360
        #platform up
        elif key == 3 and self.oz > -28.0:
            self.oz = self.oz - 0.5
        #platform down
        elif key == 4 and self.oz < 45.0:
            self.oz = self.oz + 0.5
        #reset
        elif key == 1:
            self.oz, self.oy = 0.0, 0.0
            gluLookAt(-2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glutPostRedisplay()
