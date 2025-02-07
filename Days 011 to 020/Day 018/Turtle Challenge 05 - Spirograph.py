import secrets
import turtle
import math

BACKGROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
SCREEN_DIMENSIONS: dict = {"width": 720, "height": 600}


def create_screen():
    try:
        screen = turtle.Screen()
        screen.setup(SCREEN_DIMENSIONS["width"], SCREEN_DIMENSIONS["height"])
        screen.colormode(255)
        screen.bgcolor(BACKGROUND_COLOR)
        screen.title("Turtle Challenge 05 - Spirograph")
        return screen
    except Exception as error:
        print(error)
        return None


def create_turtle(move_speed: int | str = "fast", line_thickness: int = 13, turtle_color: str = "#FF0000"):
    """
    Create a turtle.

    Args:
        move_speed(int | str): the speed that the turtle will move. Either a speed string or a number between 0 and 10.
        line_thickness(int): the thickness of the lines created by movement.
        turtle_color(str): the color of the turtle. An RGB Hex string
    """
    try:
        tim = turtle.Turtle()
        tim.color(turtle_color)
        tim.speed(move_speed)
        tim.pensize(line_thickness)
        return tim
    except Exception as error:
        print(error)
        return None


def get_random_color():
    """
    Generate a random color.

    Returns:
        tuple[int, int, int]: a tuple containing the RGB values.
    """
    colors: tuple[int, int, int] = (secrets.choice([0, 255]), secrets.choice([0, 255]), secrets.choice([0, 255]))
    if colors == BACKGROUND_COLOR:
        black: tuple[int, int, int] = (0, 0, 0)
        return black
    return colors


def draw_spirograph(circle_width: int = 80, move_count: int = 40, hide_turtle_after_finish: bool = True):
    turn_angle = math.ceil(360 / move_count)
    for i in range(move_count):
        tim.pencolor(get_random_color())
        tim.circle(circle_width)
        tim.right(turn_angle)

    if hide_turtle_after_finish:
        tim.hideturtle()


if __name__ == "__main__":
    screen = create_screen()
    if screen is None:
        exit(1)

    tim = create_turtle(move_speed=0, line_thickness=3)
    if tim is None:
        exit(1)

    draw_spirograph()

    screen.exitonclick()
    exit(0)
