import OpenGL.GL as gl 
import OpenGL.GLUT as glut 
import OpenGL.GLU as glu 

modo_ver = 1

def Camera(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity() 
    glu.gluPerspective(15.0, 1.0 , 0.1, 100)
    gl.glMatrixMode(gl.GL_MODELVIEW) 
    gl.glLoadIdentity() 

    global modo_ver

    #Três ângulos de visão diferentes
    if modo_ver == 1:
        glu.gluLookAt(2, 2, 4,  0, 0, 0,  0, 0, 1)
    elif modo_ver == 2:
        glu.gluLookAt(3, 3, 3,  0, 0, 0,  0, 1, 0)
    elif modo_ver == 3:
        glu.gluLookAt(4, 2, 1,  0, 0, 0,  0, 1, 0)
    
def display(): 
    glut.glutSwapBuffers() 
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
    
    gl.glColor3f (0.31, 0.78, 0.47) 
    glut.glutSolidCone(0.1, 0.5, 100, 100) #Cone
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
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGBA) 
glut.glutCreateWindow(b'Felipe Freire') 
glut.glutReshapeWindow(512, 512) 
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard) 
glut.glutMainLoop()