import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

rotacao_x = 0.0

def keyboard(key, x, y):
    global translacao_y, rotacao_x

    if key == b'r':  # Rotação no sentido horário no eixo X
        rotacao_x += 3.0
    elif key == b'R':  # Rotação no sentido anti-horário no eixo X
        rotacao_x -= 3.0

    glut.glutPostRedisplay()

def Camera(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity() 
    glu.gluPerspective(30.0, 1.0, 0.1, 100)
    glu.gluLookAt(3, 3, 3,  0, 0, 0,  0, 1, 0)
    gl.glMatrixMode(gl.GL_MODELVIEW) 
    gl.glLoadIdentity()

def display():
    glut.glutSwapBuffers() 
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glDisable(gl.GL_CULL_FACE)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0) 

    Camera() 

    gl.glRotatef(rotacao_x, 0, 0, 1)

    gl.glBegin(gl.GL_QUADS)

    #Face frontal(vermelho)
    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(-0.6, -0.3, 0.2)
    gl.glVertex3f(0.6, -0.3, 0.2)
    gl.glVertex3f(0.6, 0.3, 0.2)
    gl.glVertex3f(-0.6, 0.3, 0.2)

    #Face traseira(verde)
    gl.glColor3f(0, 1, 0)
    gl.glVertex3f(-0.6, -0.3, -0.2)
    gl.glVertex3f(-0.6, 0.3, -0.2)
    gl.glVertex3f(0.6, 0.3, -0.2)
    gl.glVertex3f(0.6, -0.3, -0.2)

    #Face superior(azul)
    gl.glColor3f(0, 0, 1)
    gl.glVertex3f(-0.6,  0.3, -0.2)
    gl.glVertex3f(-0.6, 0.3, 0.2)
    gl.glVertex3f(0.6, 0.3, 0.2)
    gl.glVertex3f(0.6, 0.3, -0.2)

    #Face inferior(amarelo)
    gl.glColor3f(1, 1, 0)
    gl.glVertex3f(-0.6, -0.3, -0.2)
    gl.glVertex3f(0.6, -0.3, -0.2)
    gl.glVertex3f(0.6, -0.3, 0.2)
    gl.glVertex3f(-0.6, -0.3, 0.2)

    #Face direita(roxo)
    gl.glColor3f(1, 0, 1)
    gl.glVertex3f(0.6, -0.3, -0.2)
    gl.glVertex3f(0.6, 0.3, -0.2)
    gl.glVertex3f(0.6, 0.3, 0.2)
    gl.glVertex3f(0.6, -0.3, 0.2)

    #Face esquerda(ciano)
    gl.glColor3f(0, 1, 1)
    gl.glVertex3f(-0.6, -0.3, -0.2)
    gl.glVertex3f(-0.6, -0.3, 0.2)
    gl.glVertex3f(-0.6, 0.3, 0.2)
    gl.glVertex3f(-0.6, 0.3, -0.2)

    gl.glEnd()

    gl.glFlush() 
    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()