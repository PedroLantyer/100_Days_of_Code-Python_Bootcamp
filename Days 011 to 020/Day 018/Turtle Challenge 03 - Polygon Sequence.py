import secrets
import turtle

BACKGROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
START_POSITION: dict = {"x": 40, "y": 100}


def create_screen():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Turtle Challenge 03 - Polygon Sequence")
    screen.setup(width=600, height=600)
    return screen


def create_turtle(color: str = "red", pen_color: str = "black"):
    """
    Creates a turtle

    Args:
        color (str): Color of the turtle.
        pen_color (str): The color used to draw lines.

    Returns:
        :rtype: (turtle.Turtle, None):
        - A Turtle.
        - If the function fails, return None
    """
    try:
        tim = turtle.Turtle(shape="turtle")
        tim.color(color)
        tim.pencolor(pen_color)
        tim.teleport(x=START_POSITION["x"], y=START_POSITION["y"])
        return tim

    except Exception as err:
        print(err)
        print("Failed to create turtle")
        return None


def get_random_colors():
    """
    Gets a tuple of randomized colors

    Returns:
        tuple[int, int, int]: A tuple with the RGB value
    """
    colors: list[int] = []
    for i in range(3):
        color: int = secrets.choice([0, 255])
        colors.append(color)
    color_tuple = tuple(colors)
    if color_tuple == BACKGROUND_COLOR:
        black: tuple[int, int, int] = (0, 0, 0)
        return black
    return color_tuple


def draw_polygon(tim: turtle.Turtle, side_size: int, side_count: int):
    """
    Draws a polygon

    Args:
        tim (turtle.Turtle): Turtle
        side_size(int): Size of each side of the polygon
        side_count: Number of sides for the polygon

    """
    turn_angle = 360 / side_count
    for i in range(side_count):
        tim.right(turn_angle)
        tim.forward(side_size)


if __name__ == "__main__":
    screen = create_screen()

    timmy = create_turtle()
    if timmy is None:
        exit(1)

    walking_distance = 60
    for i in range(3, 11):
        colors = get_random_colors()
        timmy.pencolor(colors)
        draw_polygon(timmy, walking_distance, i)

    screen.exitonclick()
