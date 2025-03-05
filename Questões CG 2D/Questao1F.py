import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

def desenhar_circulo(cx, cy, raio=0.5, num_segmentos=100, cor=(1, 0, 0)):
    gl.glColor3f(*cor)
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(cx, cy)
    
    for i in range(num_segmentos + 1):
        angulo = 2.0 * math.pi * i / num_segmentos
        x = cx + raio * math.cos(angulo)
        y = cy + raio * math.sin(angulo)
        gl.glVertex2f(x, y)
        
    gl.glEnd()

def display():
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    
    desenhar_circulo(0, 0, raio=0.2, cor=(1, 0.55, 0)) #meio laranja
    desenhar_circulo(0, 0.35, raio=0.25, cor=(1, 1, 0)) #cima amarelo
    desenhar_circulo(-0.35, 0, raio=0.25, cor=(1, 0, 0)) #esquerda vermelho
    desenhar_circulo(0.35, 0, raio=0.25, cor=(0, 1, 0)) #direita verde
    desenhar_circulo(0, -0.35, raio=0.25, cor=(0, 0, 1)) #baixo azul
    
    gl.glFlush()
    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutCreateWindow(b'Felipe Freire')
glut.glutReshapeWindow(512, 512)
glut.glutDisplayFunc(display)
glut.glutMainLoop()