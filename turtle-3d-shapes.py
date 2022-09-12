import turtle as t
# import random


def drawShape3d(edges_num, size):
    edge = 360 / edges_num
    x = edges_num
    while x != 0:
        t.forward((1000 / edges_num) * size)
        t.left(edge)
        x -= 1


def bevel3d(offset):
    t.backward(offset)


def tunnel3d(x, y, stretch_val=0):
    stretch = stretch_val
    t.setheading(x + y)
    # t.penup()
    t.forward(x + stretch)
    t.left(y + stretch)
    # t.pendown()


t.penup()
t.color('white')
t.pencolor('black')
t.goto(-250, -300)
t.pendown()
t.speed(0)

iterations = 100
size_iter = 1
stretch_iter = 0

while iterations != 0:
    # if iterations == 1:
    #    t.begin_fill()

    tunnel3d(5, 15, stretch_iter)
    drawShape3d(6, size_iter)

    stretch_iter += 0  # stretch size
    size_iter -= 0.01
    # iterations -= 1
t.end_fill()
t.done()
