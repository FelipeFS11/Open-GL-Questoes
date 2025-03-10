import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

#aplicar escala em tres objetos

escala_esfera_verde = [1.0, 1.0, 1.0]
escala_esfera_azul = [1.0, 1.0, 1.0]
escala_esfera_vermelha = [1.0, 1.0, 1.0]

def Camera(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity() 
    glu.gluPerspective(60, 1.0, 0.1, 50.0)
    glu.gluLookAt(0, 0, 5,  0, 0, 0,  0, 1, 0)
    gl.glMatrixMode(gl.GL_MODELVIEW) 
    gl.glLoadIdentity()

def keyboard(key, x, y):
    global escala_esfera_verde, escala_esfera_azul, escala_esfera_vermelha

    #aumentar as esferas
    if key == b'1':
        escala_esfera_verde = [escala_esfera_verde[0] * 1.1, escala_esfera_verde[1] * 1.1, escala_esfera_verde[2] * 1.1]
    elif key == b'2':
        escala_esfera_azul = [escala_esfera_azul[0] * 1.1, escala_esfera_azul[1] * 1.1, escala_esfera_azul[2] * 1.1]
    elif key == b'3':
        escala_esfera_vermelha = [escala_esfera_vermelha[0] * 1.1, escala_esfera_vermelha[1] * 1.1, escala_esfera_vermelha[2] * 1.1]

    #diminuir as esferas
    elif key == b'q': 
        escala_esfera_verde = [escala_esfera_verde[0] * 0.9, escala_esfera_verde[1] * 0.9, escala_esfera_verde[2] * 0.9]
    elif key == b'w': 
        escala_esfera_azul = [escala_esfera_azul[0] * 0.9, escala_esfera_azul[1] * 0.9, escala_esfera_azul[2] * 0.9]
    elif key == b'e': 
        escala_esfera_vermelha= [escala_esfera_vermelha[0] * 0.9, escala_esfera_vermelha[1] * 0.9, escala_esfera_vermelha[2] * 0.9]
    
    elif key == b'R':  #reseta o escalonamento
        escala_esfera_verde = [1.0, 1.0, 1.0]
        escala_esfera_azul = [1.0, 1.0, 1.0]
        escala_esfera_vermelha = [1.0, 1.0, 1.0]

    glut.glutPostRedisplay()

def desenha_esfera(cor):
    gl.glColor3f(cor[0], cor[1], cor[2])
    glut.glutSolidSphere(0.5, 20, 20) #desenha a esfera pela biblioteca do open gl

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0) 

    Camera()

    gl.glPushMatrix()
    gl.glScalef(escala_esfera_verde[0], escala_esfera_verde[1], escala_esfera_verde[2])
    gl.glTranslatef(-1.5, 0, 0) #posição
    desenha_esfera([0,1,0]) #esfera verde
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glScalef(escala_esfera_azul[0], escala_esfera_azul[1], escala_esfera_azul[2])
    gl.glTranslatef(0, 0, 0)
    desenha_esfera([0,0,1]) #esfera azul
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glScalef(escala_esfera_vermelha[0], escala_esfera_vermelha[1], escala_esfera_vermelha[2])
    gl.glTranslatef(1.5, 0, 0) 
    desenha_esfera([1,0,0]) #esfera vermelha
    gl.glPopMatrix()
    

    gl.glFlush()
    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()

