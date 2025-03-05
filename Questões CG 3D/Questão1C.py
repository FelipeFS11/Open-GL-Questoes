import OpenGL.GL as gl 
import OpenGL.GLUT as glut 
import OpenGL.GLU as glu 

modo_ver = 1

def Camera(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity() 
    glu.gluPerspective(30.0, 1.0, 0.1, 100)
    gl.glMatrixMode(gl.GL_MODELVIEW) 
    gl.glLoadIdentity() 

    global modo_ver
    
    #Três ângulos de visão diferentes
    if modo_ver == 1:
        glu.gluLookAt(2, 2, 4,  0, 0, 0,  0, 1, 0)
    elif modo_ver == 2:
        glu.gluLookAt(3, 3, 3,  0, 0, 0,  0, 1, 0)
    elif modo_ver == 3:
        glu.gluLookAt(4, 2, 1,  0, 0, 0,  0, 1, 0)

def display(): 
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) 
    gl.glClearColor(1.0, 1.0, 1.0, 1.0) 

    gl.glEnable(gl.GL_DEPTH_TEST)  

    Camera() 

    #5 vértices da base pentagonal
    v1 = (-0.5, -0.5, 0.0)
    v2 = (-0.25, -0.5, 0.45)
    v3 = (0.25, -0.5, 0.45)
    v4 = (0.5, -0.5, 0.0)
    v5 = (0.0, -0.5, -0.5)
    
    topo = (0.0, 0.5, 0.0)

    #base(vermelho)
    gl.glBegin(gl.GL_POLYGON)
    gl.glColor3f(1, 0, 0) 
    gl.glVertex3fv(v1)
    gl.glVertex3fv(v2)
    gl.glVertex3fv(v3)
    gl.glVertex3fv(v4)
    gl.glVertex3fv(v5)
    gl.glEnd()

    gl.glBegin(gl.GL_TRIANGLES)

    #Face 1(verde)
    gl.glColor3f(0, 1, 0)
    gl.glVertex3fv(v1)
    gl.glVertex3fv(v2)
    gl.glVertex3fv(topo)

    #Face 2(azul)
    gl.glColor3f(0, 0, 1)
    gl.glVertex3fv(v2)
    gl.glVertex3fv(v3)
    gl.glVertex3fv(topo)

    #Face 3(amarelo)
    gl.glColor3f(1, 1, 0) 
    gl.glVertex3fv(v3)
    gl.glVertex3fv(v4)
    gl.glVertex3fv(topo)

    #Face 4(roxo)
    gl.glColor3f(1, 0, 1)
    gl.glVertex3fv(v4)
    gl.glVertex3fv(v5)
    gl.glVertex3fv(topo)

    #Face 5(ciano)
    gl.glColor3f(0, 1, 1)
    gl.glVertex3fv(v5)
    gl.glVertex3fv(v1)
    gl.glVertex3fv(topo)

    gl.glEnd()

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
    gl.glFlush() 
    glut.glutSwapBuffers()

def keyboard(key, x, y):
    global modo_ver

    if key == b'1':
        modo_ver = 1  
    elif key == b'2':
        modo_ver = 2  
    elif key == b'3':
        modo_ver = 3 
    elif key == b'\x1b':  #ESC para sair
        glut.glutLeaveMainLoop()

    glut.glutPostRedisplay()

glut.glutInit() 
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH) 
glut.glutCreateWindow(b'Felipe Freire') 
glut.glutReshapeWindow(512, 512) 
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard) 
glut.glutMainLoop()
