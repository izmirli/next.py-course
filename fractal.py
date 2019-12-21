import turtle
import math
import colorsys


def square(t, size):
    for tmp in range(0, 4):
        t.forward(size)
        t.right(90)


def koch(p, size, level):
    # print(f'koch size: {size}, heading: {p.heading()}.')
    if level <= 1:
        p.forward(size)
    else:
        for degrees in [0, 60, -120, 60]:
            p.left(degrees)
            koch(p, size / 3, level - 1)


starting_size = 500
starting_level = 5
pen = turtle.Pen()
pen.speed(0)
pen.up()
pen.left(90)
pen.forward(starting_size / 2)
pen.right(150)
pen.down()
pen.pensize(2)
for _ in range(3):
    koch(pen, starting_size, starting_level)
    pen.right(120)

# pen.speed(0)
# phi = 180 * (3 - math.sqrt(5))
# num = 150
# shape = 'circle'  # 'square'
#
# for x in reversed(range(0, num)):
#     pen.fillcolor(colorsys.hsv_to_rgb(x / num, 1.0, 1.0))
#     pen.begin_fill()
#     if shape == 'circle':
#         pen.circle(5 + x, None, 11)
#     else:
#         square(pen, 5 + x)
#     pen.end_fill()
#     pen.right(phi)
#     pen.right(.8)
#
# turtle.mainloop()


# t = turtle.Turtle()
# t.speed(0)
# b = 180
#
# for c in range(5):
#     a = 9*c
#     for i in range(100):
#         t.circle(i, a)
#         t.right(b)
#         t.circle(i, a)
#         t.right(b)
#         t.circle(i, a)
#         t.right(b)
#         t.circle(i ,a)

input('Press any key to continue...')