import OpenGL.GL as gl
import OpenGL.GLUT as glut

def desenhar_eixos():
    gl.glLineWidth(2) #espessura da linha
    gl.glBegin(gl.GL_LINES)

    #limites eixo x
    gl.glColor3f(0.0, 0.0, 0.1) 
    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)

    #limites eixo y
    gl.glColor3f(0.0, 0.0, 0.1)
    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)

    gl.glEnd()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glLoadIdentity()
    desenhar_eixos() #chama a função dos eixos
    gl.glFlush()

    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0, 0, 0)
    gl.glVertex3f(0.4, 0.2, 0.0)
    gl.glVertex3f(0.8, 0.2, 0.0)
    gl.glVertex3f(0.6, 0.6, 0.0)
    gl.glEnd()
    gl.glFlush()

    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0, 0, 0)
    gl.glVertex3f(-0.4, 0.2, 0.0)
    gl.glVertex3f(-0.8, 0.2, 0.0)
    gl.glVertex3f(-0.6, 0.6, 0.0)
    gl.glEnd()
    gl.glFlush()

    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0, 0, 0)
    gl.glVertex3f(-0.4, -0.2, 0.0)
    gl.glVertex3f(-0.8, -0.2, 0.0)
    gl.glVertex3f(-0.6, -0.6, 0.0)
    gl.glEnd()
    gl.glFlush()

    gl.glShadeModel(gl.GL_FLAT)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(0, 0, 0)
    gl.glVertex3f(0.4, -0.2, 0.0)
    gl.glVertex3f(0.8, -0.2, 0.0)
    gl.glVertex3f(0.6, -0.6, 0.0)
    gl.glEnd()
    gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()