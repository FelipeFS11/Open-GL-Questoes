import OpenGL.GL as gl
import OpenGL.GLUT as glut

translacao_y = 0.0 
rotacao_x = 0.0

def keyboard(key, x, y):
    global translacao_y, rotacao_x

    if key == b't':  # Translação positiva no eixo Y
        translacao_y += 0.1
    elif key == b'T':  # Translação negativa no eixo Y
        translacao_y -= 0.1
    elif key == b'r':  # Rotação no sentido horário no eixo X
        rotacao_x += 5.0
    elif key == b'R':  # Rotação no sentido anti-horário no eixo X
        rotacao_x -= 5.0
    glut.glutPostRedisplay()

def display():
    glut.glutSwapBuffers()
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1, 0, 0)  #Vermelho
    gl.glVertex2f(-0.2, 0.0)
    gl.glColor3f(1, 0, 1)  #Rosa
    gl.glVertex2f(0.0, 0.2)
    gl.glColor3f(1, 1, 0)  #Amarelo
    gl.glVertex2f(0.2, 0.0)
    gl.glColor3f(0, 0, 1)  #Azul
    gl.glVertex2f(0.0, -0.2)
    gl.glEnd()

    gl.glTranslatef(0.0, translacao_y, 0.0) #translação
    gl.glRotatef(rotacao_x, 0, 0, 1) #rotação

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()

