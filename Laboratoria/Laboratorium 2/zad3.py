#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

color_bottom_left = (1.0, 1.0, 1.0)
color_top_left = (1.0, 1.0, 1.0)
color_bottom_right = (1.0, 1.0, 1.0)
color_top_right = (1.0, 1.0, 1.0)


def startup(window):
    global color_bottom_left, color_top_left, color_bottom_right, color_top_right
    width, height = glfwGetFramebufferSize(window)
    update_viewport(window, width, height)
    glClearColor(0.5, 0.5, 0.5, 1.0)

    random.seed()
    color_bottom_left = (random.random(), random.random(), random.random())
    color_top_left = (random.random(), random.random(), random.random())
    color_bottom_right = (random.random(), random.random(), random.random())
    color_top_right = (random.random(), random.random(), random.random())


def shutdown():
    pass

def draw_rectangle(x, y, a, b, d=0.0):
    a_deformed = a * (1.0 + d)
    b_deformed = b * (1.0 + d)

    glBegin(GL_TRIANGLES)

    glColor3f(*color_bottom_left)
    glVertex2f(x, y)
    glColor3f(*color_top_left)
    glVertex2f(x, y + b_deformed)
    glColor3f(*color_bottom_right)
    glVertex2f(x + a_deformed, y)

    glColor3f(*color_top_left)
    glVertex2f(x, y + b_deformed)
    glColor3f(*color_bottom_right)
    glVertex2f(x + a_deformed, y)
    glColor3f(*color_top_right)
    glVertex2f(x + a_deformed, y + b_deformed)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_rectangle(-40, -20, 80, 40, 0.4)

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
