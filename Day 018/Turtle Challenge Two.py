import turtle


def draw_dashed_line(tim: turtle.Turtle):
    for i in range(1, 51):
        tim.penup() if i % 2 == 0 else tim.pendown()
        tim.forward(10)


def create_turtle():
    tim = turtle.Turtle(shape="turtle")
    tim.teleport(x=-150, y=100)
    tim.color("red")
    tim.pencolor("black")
    return tim


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("#7d7c7c")

    timmy = create_turtle()

    draw_dashed_line(timmy)

    screen.exitonclick()
