import turtle


def draw_square():
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)


if __name__ == '__main__':
    timmy = turtle.Turtle(shape="turtle")
    timmy.color("#FF0000")
    draw_square()
    screen = turtle.Screen()
    screen.exitonclick()
