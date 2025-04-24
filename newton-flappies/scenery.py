import pygame
import random

from game_object import GameObject


#--- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 200)
GREEN1 = (0, 175, 0)
GREEN2 = (0, 150, 0)
TAN1 = (225, 225, 150)
TAN2 = (175, 175, 100)


class Sun(GameObject):

    x = 0
    y = 0
    h = 0
    w = 0
    v_x = 0
    v_y = 0
    
    
    def __init__(self, x, y, d=150):
        self.x = x
        self.y = y
        self.h = d
        self.w = d

        
    def draw(self, screen):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        
        pygame.draw.ellipse(screen, YELLOW, [x, y, w, h])


class Cloud(GameObject):

    x = 0
    y = 0
    h = 60
    w = 100
    v_x = 0
    v_y = 0


    def __init__(self, x, y, v_x=0):
        self.x = x
        self.y = y
        self.v_x = v_x


    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
        pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
        pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
        pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])


class Ground():

    x = 0
    y = 0
    w = 0
    h = 0
    stripes = []
    sand = []


    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        for i in range(0, self.w + self.h, 30):
            self.stripes.append(i)

        for i in range(self.w // 4):
            x = random.randrange(0, self.w)
            y = random.randrange(self.y + 50, self.y + 100)
            self.sand.append([x, y])

    
    def draw(self, screen):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        
        pygame.draw.rect(screen, GREEN1, [x, y, w, h//2])
        pygame.draw.rect(screen, TAN1, [x, y + h/2, w, h//2])

        for s in self.stripes:
            pygame.draw.line(screen, GREEN2, [s, y], [s - h//2, y + h//2], 10)
        
        for s in self.sand:
            pygame.draw.rect(screen, TAN2, [s[0], s[1], 2, 2])
                    
        pygame.draw.line(screen, BLACK, [x, y], [x + w, y], 2)
        pygame.draw.line(screen, BLACK, [x, y + h//2], [x + w, y + h//2], 2)
