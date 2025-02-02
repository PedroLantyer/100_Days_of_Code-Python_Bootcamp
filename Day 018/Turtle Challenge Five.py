import secrets
import turtle
import math

BACK_GROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
SCREEN_WIDTH: int = 720
SCREEN_HEIGHT: int = 480


def create_screen():
    try:
        screen = turtle.Screen()
        screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.colormode(255)
        screen.bgcolor(BACK_GROUND_COLOR)
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
        tim = turtle.Turtle(shape="turtle")
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
    if colors == BACK_GROUND_COLOR:
        black: tuple[int, int, int] = (0, 0, 0)
        return black
    return colors


def draw_spirograph(circle_width: int = 80, move_count: int = 36):
    turn_angle = math.ceil(360 / move_count)
    for i in range(move_count):
        tim.pencolor(get_random_color())
        tim.circle(circle_width)
        tim.right(turn_angle)


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
