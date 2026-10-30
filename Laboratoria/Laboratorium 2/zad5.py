#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup(window):
    width, height = glfwGetFramebufferSize(window)
    update_viewport(window, width, height)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_sierpinski_triangle(x1, y1, x2, y2, x3, y3, depth):
    if depth == 0:
        draw_triangle(x1, y1, x2, y2, x3, y3)
        return

    x12 = (x1 + x2) / 2.0
    x23 = (x2 + x3) / 2.0
    x31 = (x3 + x1) / 2.0
    y12 = (y1 + y2) / 2.0
    y23 = (y2 + y3) / 2.0
    y31 = (y3 + y1) / 2.0

    draw_sierpinski_triangle(x1, y1, x12, y12, x31, y31, depth - 1)
    draw_sierpinski_triangle(x12, y12, x2, y2, x23, y23, depth - 1)
    draw_sierpinski_triangle(x31, y31, x23, y23, x3, y3, depth - 1)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 1.0, 0.0)

    draw_sierpinski_triangle(-70.0, -60.0, 0.0, 60.0, 70.0, -60.0, depth=4)

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup(window)
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()