import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import sys

anguloX, anguloY = 0.0, 0.0
zoom = -5.0

def Camera():
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60, 1, 0.1, 50)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    glu.gluLookAt(0, 0, zoom, 0, 0, 0, 0, 1, 0)
    gl.glRotatef(anguloX, 1, 0, 0)
    gl.glRotatef(anguloY, 0, 1, 0)

vertices = [
    (-1.0, -1.0, -1.0), #0
    (1.0, -1.0, -1.0), #1
    (0.0, 1.0, -1.0), #2
    (-1.0, -1.0, 1.0), #3
    (1.0, -1.0, 1.0), #4
    (0.0, 1.0, 1.0) #5
]

faces = [
    (0, 1, 2), #base inferior
    (3, 4, 5), #base superior
    (0, 1, 4, 3), #lateral traseira
    (1, 2, 5, 4), #lateral direita
    (2, 0, 3, 5) #lateral esquerda
]

cores = [
    (1, 0, 0), #vermelho
    (0, 1, 0), #verde
    (0, 0, 1), #azul
    (1, 1, 0), #amarelo
    (1, 0, 1) #roxo
]

def prisma():
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3fv(cores[0]) 
    gl.glVertex3fv(vertices[faces[0][0]]) #armazenando cada face do prisma em vetores 
    gl.glVertex3fv(vertices[faces[0][1]])
    gl.glVertex3fv(vertices[faces[0][2]])
    
    gl.glColor3fv(cores[1])
    gl.glVertex3fv(vertices[faces[1][0]])
    gl.glVertex3fv(vertices[faces[1][1]])
    gl.glVertex3fv(vertices[faces[1][2]])
    gl.glEnd()

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3fv(cores[2])
    gl.glVertex3fv(vertices[faces[2][0]])
    gl.glVertex3fv(vertices[faces[2][1]])
    gl.glVertex3fv(vertices[faces[2][2]])
    gl.glVertex3fv(vertices[faces[2][3]])
    
    gl.glColor3fv(cores[3])
    gl.glVertex3fv(vertices[faces[3][0]])
    gl.glVertex3fv(vertices[faces[3][1]])
    gl.glVertex3fv(vertices[faces[3][2]])
    gl.glVertex3fv(vertices[faces[3][3]])
    
    gl.glColor3fv(cores[4])
    gl.glVertex3fv(vertices[faces[4][0]])
    gl.glVertex3fv(vertices[faces[4][1]])
    gl.glVertex3fv(vertices[faces[4][2]])
    gl.glVertex3fv(vertices[faces[4][3]])
    gl.glEnd()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)

    gl.glBegin(gl.GL_LINES)
    
    #Eixo X
    gl.glColor3f(0.0, 0.0, 0.0)
    gl.glVertex3f(-2.0, 0.0, 0.0)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(2.0, 0.0, 0.0)

    #Eixo Y
    gl.glColor3f(0.0, 0.0, 0.0)
    gl.glVertex3f(0.0, -2.0, 0.0)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(0.0, 2.0, 0.0)

    #Eixo Z
    gl.glColor3f(0.0, 0.0, 0.0)
    gl.glVertex3f(0.0, 0.0, -2.0)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(0.0, 0.0, 2.0)

    gl.glEnd()

    Camera()
    prisma()
    gl.glFlush()
    glut.glutSwapBuffers()

def keyboard(key, x, y):
    global zoom
    key = key.decode("utf-8")

    if key == '\x1b':
        sys.exit()
    elif key == 'w':
        zoom += 0.2
    elif key == 's':
        zoom -= 0.2

    glut.glutPostRedisplay()


def specialKeys(key, x, y):
    global anguloX, anguloY

    if key == glut.GLUT_KEY_LEFT:
        anguloY -= 5
    elif key == glut.GLUT_KEY_RIGHT:
        anguloY += 5
    elif key == glut.GLUT_KEY_UP:
        anguloX -= 5
    elif key == glut.GLUT_KEY_DOWN:
        anguloX += 5

    glut.glutPostRedisplay()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutSpecialFunc(specialKeys)
gl.glEnable(gl.GL_DEPTH_TEST)
glut.glutMainLoop()