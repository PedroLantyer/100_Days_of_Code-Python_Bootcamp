import colorgram
import turtle
import secrets

COLOR_COUNT: int = 39  # There are 39 different colors in the sample image
IMG_PATH: str = "../assets/img/hirst_color_painting.jpg"
BACKGROUND_COLOR: tuple[int, int, int] = (125, 124, 124)
SCREEN_DIMENSIONS: dict = {"width": 720, "height": 720}
START_POSITION: dict = {"x": -240, "y": -240}
HARD_CODED_COLORS: list[tuple[int, int, int]] = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17),
                                                 (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20),
                                                 (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
                                                 (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149),
                                                 (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
                                                 (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
                                                 (248, 11, 9), (222, 140, 203), (68, 240, 161),
                                                 (10, 97, 62),
                                                 (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208),
                                                 (86, 225, 235), (250, 8, 14), (242, 166, 157),
                                                 (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]


def extract_colors():
    try:
        colors = colorgram.extract(f=IMG_PATH, number_of_colors=COLOR_COUNT)
        color_list: list[tuple[int, int, int]] = []
        for color in colors:
            color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
        return color_list
    except Exception as error:
        print("Failed to extract colors from image")
        print(error)
        return None


def create_screen():
    try:
        screen = turtle.Screen()
        screen.title("Hirst Painting")
        screen.setup(width=SCREEN_DIMENSIONS["width"], height=SCREEN_DIMENSIONS["height"])
        screen.colormode(255)
        screen.bgcolor(BACKGROUND_COLOR)
        return screen
    except Exception as error:
        print("Failed to create screen")
        print(error)
        return None


def create_turtle(move_speed: int | str = "fast", turtle_color: str = "#000000", visible: bool = False):
    """
    Create a turtle.

    Args:
        move_speed(int | str): the speed that the turtle will move. Either a speed string or a number between 0 and 10.

        turtle_color(str): the color of the turtle. An RGB Hex string
        visible(bool): if True the turtle will appear in the screen.
    """
    try:
        tim = turtle.Turtle(visible=visible)
        tim.color(turtle_color)
        tim.speed(move_speed)
        return tim
    except Exception as error:
        print("Failed to create turtle")
        print(error)
        return None


def draw_painting(tim: turtle.Turtle, colors: list[tuple[int, int, int]], row_count: int = 10, column_count: int = 10,
                  dot_size: int = 20, dot_spacing: int = 50):
    for i in range(row_count):
        for j in range(column_count):
            tim.dot(dot_size, secrets.choice(colors))
            tim.forward(dot_spacing)
        tim.teleport(y=int(tim.ycor()) + dot_spacing, x=START_POSITION["x"])


if __name__ == '__main__':
    use_hard_coded_colors: bool = True
    colors = HARD_CODED_COLORS if use_hard_coded_colors else extract_colors()
    if colors is None:
        exit(1)

    screen = create_screen()
    if screen is None:
        exit(1)

    tim = create_turtle()
    if tim is None:
        exit(1)

    tim.teleport(x=START_POSITION["x"], y=START_POSITION["y"])  # Set the starting position for the turtle
    tim.penup()  # Prevent line drawing

    draw_painting(tim=tim, colors=colors)
    screen.exitonclick()
    exit(0)
