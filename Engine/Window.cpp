#include "Window.h"

#include "../includes/glfw3.h"

Window::Window() {
    this->init();
}

bool Window::init() {
    if (!glfwInit()) return false;

    GLFWwindow * window = glfwCreateWindow(800, 600, "My Window", NULL, NULL);

    if (!window) {
        glfwTerminate();
        return false;
    }

    glfwMakeContextCurrent(window);

    return false;
}

bool Window::release() {
    glfwTerminate();
    return true;
}

Window::~Window() {
    this->release();
}
