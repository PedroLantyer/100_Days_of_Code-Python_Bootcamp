import turtle

START_POSITION: dict = {"x": -220, "y": 100}
BACKGROUND_COLOR: str = "#7d7c7c"


def draw_dashed_line(tim: turtle.Turtle):
    for i in range(1, 51):
        tim.penup() if i % 2 == 0 else tim.pendown()
        tim.forward(10)


def create_screen():
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Turtle Challenge 02 - Dashed Line")
    return screen


def create_turtle(color: str = "red", line_color: str = "black"):
    try:
        tim = turtle.Turtle(shape="turtle")
        tim.teleport(x=START_POSITION["x"], y=START_POSITION["y"])
        tim.color(color)
        tim.pencolor(line_color)
        return tim
    except Exception as error:
        print(error)
        print("Failed to create turtle.")
        return None


if __name__ == "__main__":
    screen = create_screen()
    timmy = create_turtle()
    if timmy is None:
        exit(1)

    draw_dashed_line(timmy)

    screen.exitonclick()
    exit(0)
