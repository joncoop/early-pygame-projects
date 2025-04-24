import pygame
from game_object import GameObject

#--- Colors ---
RED = (200, 0 , 0)
YELLOW = (255, 255, 125)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Flappy(GameObject):

    # Class attributes
    x = 0
    y = 0
    h = 50
    w = 50
    v_x = 0
    v_y = 0

    h_speed = 5
    v_speed = 5

    
    # Constructor
    def __init__(self, x=0, y=0, color=RED, right=True):
        self.x = x
        self.y = y
        self.color = color
        self.right = right
        
        self.v_x = 0
        self.v_y = 0
        self.alive = True


    # Methods
    def move(self):
        self.x += self.v_x

        if self.v_y > 0:
            self.y -= self.v_y ** 2
        else:
            self.y += 0.25 * self.v_y ** 2

        self.v_y -= 1


    def flap(self):
        if self.right:
            self.v_x = self.h_speed
        else:
            self.v_x = -self.h_speed
            
        self.v_y = self.v_speed


    def face_right(self):
        self.right = True


    def face_left(self):
        self.right = False


    def lay_egg(self):
        return Egg(self.x + 15, self.y + 15)


    def die(self):
        self.alive = False

        
    def draw(self, screen):

        ''' so we don't have to keep referring to self in draw statements '''
        x = self.x
        y = self.y
        alive = self.alive
        color = self.color
        
        pygame.draw.rect(screen, color, [x, y, 50, 50])
        pygame.draw.rect(screen, BLACK, [x, y, 50, 50], 2)

        if self.right:
            pygame.draw.polygon(screen, YELLOW, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x + 50, y + 20], [x + 60, y + 25], [x + 50, y + 30]], 2)
            pygame.draw.rect(screen, color, [x - 10, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x - 10, y + 20, 40, 10], 2)

            if alive:
                pygame.draw.rect(screen, WHITE, [x + 35, y + 5, 10, 10])
                pygame.draw.rect(screen, BLACK, [x + 35, y + 5, 10, 10], 2)
                pygame.draw.rect(screen, BLACK, [x + 40, y + 10, 5, 5])
            else:
                pygame.draw.line(screen, BLACK, [x + 35, y+ 5], [x+45, y+15], 2)
                pygame.draw.line(screen, BLACK, [x + 45, y+5], [x+35, y+15], 2)
        else:
            pygame.draw.polygon(screen, YELLOW, [[x, y + 20], [x - 10, y + 25], [x, y + 30]])
            pygame.draw.polygon(screen, BLACK, [[x, y + 20], [x -10, y + 25], [x, y + 30]], 2)
            pygame.draw.rect(screen, color, [x + 20, y + 20, 40, 10])
            pygame.draw.rect(screen, BLACK, [x + 20, y + 20, 40, 10], 2)
            
            if alive:
                pygame.draw.rect(screen, WHITE, [x + 5, y + 5, 10, 10])
                pygame.draw.rect(screen, BLACK, [x + 5, y + 5, 10, 10], 2)
                pygame.draw.rect(screen, BLACK, [x + 5, y + 10, 5, 5])
            else:
                pygame.draw.line(screen, BLACK, [x + 5, y + 5], [x + 15, y + 15], 2)
                pygame.draw.line(screen, BLACK, [x + 15, y + 5], [x + 5, y + 15], 2)    



class Egg(GameObject):

    x = 0
    y = 0
    h = 25
    w = 20
    v_x = 0
    v_y = 0


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0


    def draw(self, screen):

        x = self.x
        y = self.y
        w = self.w
        h = self.h

        pygame.draw.ellipse(screen, WHITE, [x, y, w, h])
        pygame.draw.ellipse(screen, BLACK, [x, y, w, h], 2)

