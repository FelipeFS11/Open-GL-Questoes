import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

# Variáveis globais de escala
escala_esfera1 = [1.0, 1.0, 1.0]
escala_esfera2 = [1.0, 1.0, 1.0]
escala_esfera3 = [1.0, 1.0, 1.0]

# Função de configuração da câmera
def Camera(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity() 
    glu.gluPerspective(30.0, 1.0, 0.1, 100)
    glu.gluLookAt(3, 3, 3,  0, 0, 0,  0, 1, 0)
    gl.glMatrixMode(gl.GL_MODELVIEW) 
    gl.glLoadIdentity()

# Função de tratamento de teclas
def keyboard(key, x, y):
    global escala_esfera1, escala_esfera2, escala_esfera3

    if key == b'1':  # Aumentar a escala da esfera 1
        escala_esfera1 = [escala_esfera1[0] * 1.1, escala_esfera1[1] * 1.1, escala_esfera1[2] * 1.1]
    elif key == b'2':  # Aumentar a escala da esfera 2
        escala_esfera2 = [escala_esfera2[0] * 1.1, escala_esfera2[1] * 1.1, escala_esfera2[2] * 1.1]
    elif key == b'3':  # Aumentar a escala da esfera 3
        escala_esfera3 = [escala_esfera3[0] * 1.1, escala_esfera3[1] * 1.1, escala_esfera3[2] * 1.1]
    
    elif key == b'q':  # Diminuir a escala da esfera 1
        escala_esfera1 = [escala_esfera1[0] * 0.9, escala_esfera1[1] * 0.9, escala_esfera1[2] * 0.9]
    elif key == b'w':  # Diminuir a escala da esfera 2
        escala_esfera2 = [escala_esfera2[0] * 0.9, escala_esfera2[1] * 0.9, escala_esfera2[2] * 0.9]
    elif key == b'e':  # Diminuir a escala da esfera 3
        escala_esfera3 = [escala_esfera3[0] * 0.9, escala_esfera3[1] * 0.9, escala_esfera3[2] * 0.9]
    
    elif key == b'R':  # Resetar escalonamento
        escala_esfera1 = [1.0, 1.0, 1.0]
        escala_esfera2 = [1.0, 1.0, 1.0]
        escala_esfera3 = [1.0, 1.0, 1.0]

    glut.glutPostRedisplay()  # Atualiza a tela após pressionar uma tecla

# Função para desenhar uma esfera
def desenha_esfera():
    gl.glColor3f(0, 1, 0)  # Cor verde
    glut.glutSolidSphere(0.5, 20, 20)

# Função de exibição dos objetos na tela
def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glDisable(gl.GL_CULL_FACE)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0) 

    Camera()

    # Desenha a esfera 1
    gl.glPushMatrix()
    gl.glScalef(escala_esfera1[0], escala_esfera1[1], escala_esfera1[2])  # Aplica o escalonamento
    gl.glTranslatef(-1.5, 0, 0)  # Posição da esfera 1
    desenha_esfera()
    gl.glPopMatrix()

    # Desenha a esfera 2
    gl.glPushMatrix()
    gl.glScalef(escala_esfera2[0], escala_esfera2[1], escala_esfera2[2])  # Aplica o escalonamento
    gl.glTranslatef(0, 0, 0)  # Posição da esfera 2
    desenha_esfera()
    gl.glPopMatrix()

    # Desenha a esfera 3
    gl.glPushMatrix()
    gl.glScalef(escala_esfera3[0], escala_esfera3[1], escala_esfera3[2])  # Aplica o escalonamento
    gl.glTranslatef(1.5, 0, 0)  # Posição da esfera 3
    desenha_esfera()
    gl.glPopMatrix()

    gl.glFlush()
    glut.glutSwapBuffers()

# Função principal de inicialização
glut.glutInit()
glut.glutInitDisplayMode(0)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
