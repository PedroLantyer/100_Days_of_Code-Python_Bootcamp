import secrets
import turtle
import math

BACKGROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
SCREEN_WIDTH: int = 720
SCREEN_HEIGHT: int = 480
EAST_BOUNDARY: int = math.floor((SCREEN_WIDTH / 2) * 0.8)
WEST_BOUNDARY: int = EAST_BOUNDARY * (-1)
NORTH_BOUNDARY: int = math.floor((SCREEN_HEIGHT / 2) * 0.8)
SOUTH_BOUNDARY: int = NORTH_BOUNDARY * (-1)
WALKING_DISTANCE: int = 35


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


def get_random_movement(tim: turtle.Turtle, walking_distance: int):
    """
    Generate a random movement.

    Args:
        tim (turtle.Turtle): the turtle that will be moved.
        walking_distance (int): the distance that the turtle will move.
    """
    directions: list[str] = ["North", "East", "South", "West"]
    direction: str = secrets.choice(directions)
    match direction:
        case "East":
            tim.setheading(0)
        case "North":
            tim.setheading(90)
        case "West":
            tim.setheading(180)
        case "South":
            tim.setheading(270)

    tim.forward(walking_distance)

    # Prevent out of bounds
    x_pos, y_pos = tim.xcor(), tim.ycor()
    if (x_pos >= EAST_BOUNDARY or
            x_pos <= WEST_BOUNDARY or
            y_pos >= NORTH_BOUNDARY or
            y_pos <= SOUTH_BOUNDARY):
        tim.back(walking_distance * 1.1)


def create_screen():
    try:
        screen = turtle.Screen()
        screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.colormode(255)
        screen.bgcolor(BACKGROUND_COLOR)
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


if __name__ == "__main__":
    screen = create_screen()
    if screen is None:
        exit(1)

    tim = create_turtle()
    if tim is None:
        exit(1)

    move_count: int = 200

    for i in range(move_count):
        new_color: tuple[int, int, int] = get_random_color()
        tim.pencolor(new_color)
        get_random_movement(tim, WALKING_DISTANCE)

    screen.exitonclick()
    exit(0)
