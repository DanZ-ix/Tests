import pygame
import random

pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
WHITEBLUE = (128, 166, 255)
PURPLE = (139, 0, 255)

# Set the height and width of the screen
size = [800, 400]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Прога для Юли")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

text_color = BLACK
text_width = 3

# Начало это левый нижний угол надписи

hight = 100
kolvo_Bukv = 10

time = 0

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(5)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)

    time += 1

    if time % 7 == 0:
        text_color = RED

    if time % 7 == 1:
        text_color = ORANGE

    if time % 7 == 2:
        text_color = YELLOW

    if time % 7 == 3:
        text_color = GREEN

    if time % 7 == 4:
        text_color = WHITEBLUE

    if time % 7 == 5:
        text_color = BLUE

    if time % 7 == 6:
        text_color = PURPLE

    if time % 3 == 0:
        text_width = 3
    if time % 3 == 1:
        text_width = 5
    if time % 3 == 2:
        text_width = 9

    nadpis_nach = [int(size[0] / 10), (int(size[1] / 8) * 5)]

    if time % 2 == 1:
        randX = random.randint(-30, 30)
        randY = random.randint(-20, 20)
        nadpis_nach[0] += randX
        nadpis_nach[1] += randY

    razmer_bukvi = int((size[0] / 4 * 3) / kolvo_Bukv)
    probel = razmer_bukvi * 1 / 5

    # БУква Л

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0] + int((razmer_bukvi - probel) / 2),
                                                   nadpis_nach[1] - hight],
                                                  [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1]],
                                                  ], text_width)

    nadpis_nach[0] += razmer_bukvi

    # BUkVA Ю

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0], nadpis_nach[1] - hight],
                                                  [nadpis_nach[0], nadpis_nach[1] - hight / 2],
                                                  [int(nadpis_nach[0] + (razmer_bukvi - probel) / 2),
                                                   nadpis_nach[1] - hight / 2]], text_width)

    pygame.draw.ellipse(screen, text_color,
                        [int(nadpis_nach[0] + (razmer_bukvi - probel) / 2), hight * 1.5, (razmer_bukvi - probel) / 2,
                         hight],
                        text_width)

    nadpis_nach[0] += razmer_bukvi

    # BUKVA Б

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0], nadpis_nach[1] - hight],
                                                  [nadpis_nach[0] + hight * 3 / 8, nadpis_nach[1] - hight]], text_width)

    pygame.draw.circle(screen, text_color, [nadpis_nach[0], int(nadpis_nach[1] - hight * 3 / 8)],
                       hight * 3 / 8, text_width, draw_top_right=True, draw_bottom_right=True)

    nadpis_nach[0] += razmer_bukvi

    #  BUKVA Л

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0] + int((razmer_bukvi - probel) / 2),
                                                   nadpis_nach[1] - hight],
                                                  [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1]],
                                                  ], text_width)

    nadpis_nach[0] += razmer_bukvi

    # BUkVA Ю

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0], nadpis_nach[1] - hight],
                                                  [nadpis_nach[0], nadpis_nach[1] - hight / 2],
                                                  [int(nadpis_nach[0] + (razmer_bukvi - probel) / 2),
                                                   nadpis_nach[1] - hight / 2]], text_width)

    pygame.draw.ellipse(screen, text_color,
                        [int(nadpis_nach[0] + (razmer_bukvi - probel) / 2), hight * 1.5, (razmer_bukvi - probel) / 2,
                         hight],
                        text_width)

    nadpis_nach[0] += razmer_bukvi

    # ПРОБЕЛ
    nadpis_nach[0] += razmer_bukvi

    # БУКВА Т

    pygame.draw.line(screen, text_color, [nadpis_nach[0] + int((razmer_bukvi - probel) / 2), nadpis_nach[1] - hight],
                     [nadpis_nach[0] + int((razmer_bukvi - probel) / 2), nadpis_nach[1]], text_width)

    pygame.draw.line(screen, text_color, [nadpis_nach[0], nadpis_nach[1] - hight],
                     [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight], text_width)

    nadpis_nach[0] += razmer_bukvi
    # БУКВА Е

    pygame.draw.lines(screen, text_color, False,
                      [nadpis_nach,
                       [nadpis_nach[0], nadpis_nach[1] - hight],
                       [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight]],
                      text_width)

    pygame.draw.line(screen, text_color, [nadpis_nach[0], nadpis_nach[1] - hight / 2],
                     [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight / 2], text_width)

    pygame.draw.line(screen, text_color, [nadpis_nach[0], nadpis_nach[1]],
                     [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1]], text_width)

    nadpis_nach[0] += razmer_bukvi

    # BUKVA Б

    pygame.draw.lines(screen, text_color, False, [nadpis_nach,
                                                  [nadpis_nach[0], nadpis_nach[1] - hight],
                                                  [nadpis_nach[0] + hight * 3 / 8, nadpis_nach[1] - hight]], text_width)

    pygame.draw.circle(screen, text_color, [nadpis_nach[0], int(nadpis_nach[1] - hight * 3 / 8)],
                       hight * 3 / 8, text_width, draw_top_right=True, draw_bottom_right=True)

    nadpis_nach[0] += razmer_bukvi

    # БУКВА Я

    pygame.draw.lines(screen, text_color, False, [[nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1]],
                                                  [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight],
                                                  [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight / 2],
                                                  nadpis_nach], text_width)

    pygame.draw.circle(screen, text_color,
                       [nadpis_nach[0] + razmer_bukvi - probel, nadpis_nach[1] - hight * 3 / 4],
                       hight / 4, text_width, draw_top_left=True, draw_bottom_left=True)

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
