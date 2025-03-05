import OpenGL.GL as gl
import OpenGL.GLUT as glut


def display():
    glut.glutSwapBuffers()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)

    gl.glShadeModel(gl.GL_SMOOTH)
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(-0.8, -0.5, 0.0)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(0.8, -0.5, 0.0)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(0.8, 0.5, 0.0)
    gl.glVertex3f(-0.8, 0.5, 0.0)
    gl.glEnd()
    gl.glFlush()


glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()
