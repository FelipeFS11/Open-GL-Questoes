import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import numpy as np

#aplicar cisalahmento em uma esfera

cisalhamento = 0

def desenha_eixos():
    gl.glLineWidth(2)
    gl.glBegin(gl.GL_LINES)

    #eixo X (Vermelho)
    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(-1, 0, 0)
    gl.glVertex3f(1, 0, 0)

    #eixo Y (Verde)
    gl.glColor3f(0, 1, 0)
    gl.glVertex3f(0, -1, 0)
    gl.glVertex3f(0, 1, 0)

    #eixo Z (Azul)
    gl.glColor3f(0, 0, 1)
    gl.glVertex3f(0, 0, -1)
    gl.glVertex3f(0, 0, 1)

    gl.glEnd()

def cisalhamento_matriz(shear_x=0, shear_y=0):
    #matriz de cisalhamento aplicada no eixo y
    return np.array([
        [1, shear_x, 0, 0],
        [shear_y, 1,  0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ], dtype=np.float32)

def desenha_esfera():

    gl.glPushMatrix()

    #aplica a matriz de cisalhamento
    matriz_cisalhamento = cisalhamento_matriz(shear_x=cisalhamento, shear_y=0)
    gl.glMultMatrixf(matriz_cisalhamento)

    gl.glColor3f(1, 0.5, 0) #esfera laranja
    quad = glu.gluNewQuadric()
    glu.gluSphere(quad, 0.3, 30, 30)

    gl.glPopMatrix()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    glu.gluLookAt(0, 0.5, 1.5,  0, 0, 0,  0, 1, 0)

    desenha_eixos() 
    desenha_esfera()

    glut.glutSwapBuffers()

def keyboard(key, x, y):
    global cisalhamento

    if key == b' ':
        cisalhamento = 0.5  #ativa po achatamento
    elif key == b'r':
        cisalhamento = 0.0  #reseta

    glut.glutPostRedisplay()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(600, 600)
    glut.glutCreateWindow(b"Felipe Freire")

    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45, 1, 0.1, 10)

    gl.glMatrixMode(gl.GL_MODELVIEW)

    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()

main()
