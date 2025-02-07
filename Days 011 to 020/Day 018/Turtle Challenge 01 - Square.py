import turtle

BACKGROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
SCREEN_DIMENSIONS: dict = {"width": 480, "height": 480}


def draw_square(tim: turtle.Turtle):
    for i in range(4):
        tim.forward(100)
        tim.right(90)


def create_turtle(color: str = "red"):
    try:
        timmy = turtle.Turtle(shape="turtle")
        timmy.color(color)
        return timmy
    except Exception as error:
        print(error)
        print("Failed to create turtle")
        return None


def create_screen():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Turtle Challenge 01 - Square")
    screen.setup(width=SCREEN_DIMENSIONS["width"], height=SCREEN_DIMENSIONS["height"])
    return screen


if __name__ == '__main__':
    tim = create_turtle()
    if tim is None:
        exit(1)

    screen = create_screen()
    draw_square(tim)
    screen.exitonclick()
    exit(0)
