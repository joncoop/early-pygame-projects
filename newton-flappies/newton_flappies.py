#--- Imports ---
import pygame
import math
import random

from flappy import Flappy
from player import Player
from scenery import Cloud, Sun, Ground


#--- Initialze pygame ---
pygame.init()


#--- Colors ---
BLACK = (0, 0, 0)
SKY = (125, 175, 225)
RED = (250, 0, 0)
ORANGE = (250, 125, 0)
YELLOW = (250, 250, 0)
GREEN = (0, 250, 0)
BLUE = (0, 250, 250)
INDIGO = (0, 75, 250)
VIOLET = (150, 0, 250)


#--- Sounds ---
CLANK = pygame.mixer.Sound("sounds/clank.ogg")


#--- Window settings ---
TITLE = "Newton Flappies"
WIDTH = 800
HEIGHT = 600
FPS = 50


#--- Scenery objects ---

''' sun '''
x = int(0.75 * WIDTH)
y = int(0.10 * HEIGHT)
d = 75

sun = Sun(x, y, d)

''' clouds '''
num_clouds = 10

clouds = []
cloud_boundary_x = int(1.5 * WIDTH)
cloud_boundary_y = int(0.25 * HEIGHT)

for i in range(num_clouds):
    x = random.randrange(-cloud_boundary_x, cloud_boundary_x)
    y = random.randrange(0, cloud_boundary_y)
    v_x = -1

    c = Cloud(x, y, v_x)
    clouds.append(c)

''' ground '''
ground = Ground(0, HEIGHT - 100, WIDTH, 100)


''' list of all scenery (be sure to add in order to be drawn) '''
scenery = []
scenery += [sun]
scenery += clouds
scenery += [ground]


#--- Game objects ---

''' flappies '''
f1 = Flappy(225, 300, RED)
f2 = Flappy(275, 300, ORANGE)
f3 = Flappy(325, 300, YELLOW)
f4 = Flappy(375, 300, GREEN)
f5 = Flappy(425, 300, BLUE)
f6 = Flappy(475, 300, INDIGO)
f7 = Flappy(525, 300, VIOLET)
flappies = [f1, f2, f3, f4, f5, f6, f7]

strings = []
for f in flappies:
    strings.append([f.x  + 25, f.y - 200])


#--- Make window ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


#--- Make it go ---

flappies[0].x -= 150
flappies[0].v_x = 10
flappies[0].v_y = 0


#--- Game loop ---

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            pass

    # Game logic
    ''' move clouds '''
    for c in clouds:
        c.move()

        ''' boundary edge detection '''
        if c.x < -cloud_boundary_x:
            c.x = random.randrange(WIDTH, cloud_boundary_x)
            c.y = random.randrange(0, cloud_boundary_y)

    ''' move flappies horizontally '''
    for f in flappies:
        f.x += f.v_x

        if f.x > 700:
            f.x = 700;
            f.v_x *= -1
        elif f.x < 100:
            f.x = 100
            f.v_x *= -1

    ''' move flappies in y (string length) '''
    flappies[0].y = strings[0][1] + math.sqrt(202**2 - (flappies[0].x - strings[0][0])**2)
    flappies[6].y = strings[6][1] + math.sqrt(202**2 - (flappies[6].x - strings[6][0])**2)

    ''' check impacts '''
    for f in flappies:
        for f2 in flappies:
            if f != f2 and f.intersects(f2):

                if f.v_x > 0 and f.x < f2.x:
                    f.x = f2.x - 50
                    f2.x += 1
                    f.v_x, f2.v_x = f2.v_x, f.v_x
                elif f.v_x < 0 and f.x > f2.x:
                    f.x = f2.x + 50
                    f2.x -= 1
                    f.v_x, f2.v_x = f2.v_x, f.v_x

            if f2.v_x > 0:
                f2.right = True
            elif f2.v_x < 0:
                f2.right = False


    # Drawing code
    screen.fill(SKY)

    for s in scenery:
        s.draw(screen)

    pygame.draw.line(screen, BLACK, [0, 100], [WIDTH, 100], 10)
    for i in range(len(strings)):
        pygame.draw.line(screen, BLACK, strings[i], [flappies[i].x +25, flappies[i].y + 25], 2)


    for f in flappies:
        f.draw(screen)


    # Update screen
    pygame.display.flip()
    clock.tick(FPS)


#--- Close window on quit ---
pygame.quit()
