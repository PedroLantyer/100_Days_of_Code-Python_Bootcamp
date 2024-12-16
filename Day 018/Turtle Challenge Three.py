import math
import secrets
import turtle

BACK_GROUND_COLOR = (125, 124, 124)


def create_turtle(color: str = "red", pen_color: str = "black", start_pos: tuple[int, int] | None = None):
    """
    Creates a turtle

    Args:
        color (str): Color of the turtle.
        pen_color (str): The color used to draw lines.
        start_pos (tuple[int, int]): A tuple containing the starting X and Y coordinates for the turtle.

    Returns:
        :rtype: (turtle.Turtle, None):
        - A Turtle.
        - If the function fails, return None
    """
    try:
        if start_pos is None:
            start_pos = (-100, 100)
        tim = turtle.Turtle(shape="turtle")
        tim.color(color)
        tim.pencolor(pen_color)
        tim.teleport(x=start_pos[0], y=start_pos[1])
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
    if color_tuple == BACK_GROUND_COLOR:
        black: tuple[int, int, int] = (0, 0, 0)
        return black
    return color_tuple


def draw_triangle(tim: turtle.Turtle, hypotenuse: int):
    catethus: float = math.sqrt((hypotenuse ** 2) / 2)
    for i in range(3):
        tim.left((i+1) * 45) if i == 0 else tim.right((i+1) * 45)
        tim.forward(hypotenuse if i == 2 else catethus)


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
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(BACK_GROUND_COLOR)

    timmy: turtle.Turtle | None = create_turtle()
    if timmy is None:
        exit(1)

    walking_distance = 60
    draw_triangle(timmy, walking_distance)
    for i in range(4, 11):
        colors = get_random_colors()
        timmy.pencolor(colors)
        draw_polygon(timmy, walking_distance, i)

    screen.exitonclick()
