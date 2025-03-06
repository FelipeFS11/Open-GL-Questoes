import OpenGL.GL as gl
import OpenGL.GLUT as glut

espelhamento_x = 1
espelhamento_y = 1

def init():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-1, 1, -1, 1, -1, 1)

def desenha_eixos():
    gl.glLineWidth(2)

    #eixo x
    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(0, 0, 1)
    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)
    gl.glEnd()

    #eixo y
    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(0, 1, 0)
    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)
    gl.glEnd()


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glLoadIdentity()

    desenha_eixos()
        
    gl.glColor3f(1, 0, 0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-0.3 * espelhamento_x, -0.2 * espelhamento_y)
    gl.glVertex2f( 0.3 * espelhamento_x, -0.2 * espelhamento_y)
    gl.glVertex2f( 0.0 * espelhamento_x,  0.4 * espelhamento_y)
    gl.glEnd()

    gl.glFlush()

def keyboard(key, x, y):
    global espelhamento_x, espelhamento_y

    if key == b'x':  #espelha no eixo X
        espelhamento_x *= -1
    elif key == b'y':  #espelha no eixo Y
        espelhamento_y *= -1
    elif key == b'r':  #reseta
        espelhamento_x = 1
        espelhamento_y = 1

    glut.glutPostRedisplay()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutInitWindowSize(512, 512)
glut.glutCreateWindow(b"Felipe Freire")
init()
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
