import matplotlib.pyplot as plt

""" Reference: https://stackoverflow.com/questions/51464455/
why-when-import-pygame-it-prints-the-version-and-welcome-message-how-delete-it/51470016"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import random

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0, 0, 0)
COUNT_4 = 0
LABELS = ["A(1,2)", "B(3,4)", "C(5,6)", "S"]
POINTS = [(100, 200), (400, 400), (700, 300), (500, 500)]
X_LIST = []
Y_LIST = []


def create_labels(label_text):
    """
    Creates label and renders or blits it on screen.
    :param label_text: string
    :return label: label object
    """

    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 25)

    label = font_renderer.render(
        label_text,
        1,
        BLACK)

    return label


def draw_point_pygame(disp, index, current_xy):
    """
    Function to draw point
    :param disp: pygame screen object
    :param index: int
    :param current_xy: tuple of int
    :return: point : tuple
    """
    x_point = int((POINTS[index][0] + current_xy[0]) / 2)
    y_point = int((POINTS[index][1] + current_xy[1]) / 2)
    disp.set_at((x_point, y_point), BLACK)
    pygame.display.update()

    return x_point, y_point


def draw_point_matplotlib(index, current_xy):
    """
    Function to draw point
    :param index: int
    :param current_xy: tuple of int
    :return: point : tuple
    """

    x_point = int((POINTS[index][0] + current_xy[0]) / 2)
    y_point = int((POINTS[index][1] + current_xy[1]) / 2)
    X_LIST.append(x_point)
    Y_LIST.append(y_point)

    return x_point, y_point


def plot_pygame():
    """
    function using pygame
    """
    global COUNT_4
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.fill(WHITE)
    pygame.display.update()

    while COUNT_4 != 4:
        print("inside loop")
        label_created = create_labels(LABELS[COUNT_4])
        screen.set_at(POINTS[COUNT_4], BLACK)
        screen.blit(label_created, POINTS[COUNT_4])
        pygame.display.update()
        COUNT_4 += 1

    current_point = POINTS[3]

    for i in range(1000000):
        dice = random.randint(1, 6)
        if dice in [1, 2]:
            current_point = draw_point_pygame(screen, 0, current_point)
        elif dice in [3, 4]:
            current_point = draw_point_pygame(screen, 1, current_point)
        elif dice in [5, 6]:
            current_point = draw_point_pygame(screen, 2, current_point)
    print("The end")
    while True:
        pass


def plot_matplotlib():
    """
    function using matplotlib
    """

    current_point = POINTS[3]
    for i in range(1000000):
        dice = random.randint(1, 6)

        if dice in [1, 2]:
            current_point = draw_point_matplotlib(0, current_point)
        elif dice in [3, 4]:
            current_point = draw_point_matplotlib(1, current_point)
        elif dice in [5, 6]:
            current_point = draw_point_matplotlib(2, current_point)

    plt.axis([-800, 800, -600, 600])
    plt.plot(X_LIST, Y_LIST, 'b.')
    plt.show()


def get_user_response():
    """
    Function to get user input
    :return: response : str
    """
    print(" ")
    print("--------------Welcome to chaos---------------")
    print(" ")
    print("Do you prefer to use matplotlib or pygame for visuals ? Type m for matplotlib and p for pygame.")
    response = input(">> ")

    return response


def main():
    """
    Main function.
    :return: None
    """
    while True:
        response = get_user_response()
        if response == "m":
            plot_matplotlib()
            break
        elif response == "p":
            plot_pygame()
            break
        else:
            print("Wrong choice. So asking again")


if __name__ == "__main__":
    main()
