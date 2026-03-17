from OpenGL.GL import (
    glClear,
    glBegin,
    glColor3f,
    glVertex2f,
    glEnd,
    glFlush,
    GL_COLOR_BUFFER_BIT,
    GL_TRIANGLES
)

from OpenGL.GLUT import (
    glutInit,
    glutInitDisplayMode,
    glutInitWindowSize,
    glutCreateWindow,
    glutDisplayFunc,
    glutMainLoop,
    GLUT_SINGLE,
    GLUT_RGB
)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)   # Red color
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()

    glFlush() #ensure all openGL Command are executed

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Simple Triangle")
glutDisplayFunc(draw)
glutMainLoop()
