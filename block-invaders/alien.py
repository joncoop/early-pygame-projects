import colors
import pygame

from game_object import GameObject


class Alien(GameObject):

    def __init__(self, x, y, value=10):

        w = 40  # make sure h, w is consistent with draw function
        h = 40

        v_x = 3
        v_y = 0

        self.value = value

        super().__init__(x, y, w, h, v_x, v_y)


    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.rect(screen, colors.RED, [x, y, 40, 40])


class TieFighter(Alien):

    def __init__(self, x, y):
        value = 30
        super().__init__(x, y, value)

    def draw(self, screen):
        x = self.x
        y = self.y

        pygame.draw.rect(screen, colors.RED, [x, y, 5, 40])
        pygame.draw.rect(screen, colors.RED, [x + 35, y, 5, 40])
        pygame.draw.rect(screen, colors.RED, [x, y + 18, 40, 4])
        pygame.draw.rect(screen, colors.RED, [x + 10, y + 10, 20, 20])
        pygame.draw.rect(screen, colors.BLACK, [x + 15, y + 15, 10, 10])


class Bug(Alien):

    def __init__(self, x, y):
        value = 20
        super().__init__(x, y, value)

    def draw(self, screen):
        x = self.x
        y = self.y

        pygame.draw.rect(screen, colors.RED, [x + 10, y, 5, 40])
        pygame.draw.rect(screen, colors.RED, [x + 25, y, 5, 40])
        pygame.draw.rect(screen, colors.RED, [x, y + 25, 40, 5])
        pygame.draw.rect(screen, colors.RED, [x + 5, y + 10, 30, 25])
        pygame.draw.rect(screen, colors.BLACK, [x + 10, y + 15, 5, 5])
        pygame.draw.rect(screen, colors.BLACK, [x + 25, y + 15, 5, 5])
        pygame.draw.rect(screen, colors.BLACK, [x + 10, y + 25, 20, 5])


class Scrubby(Alien):

    def __init__(self, x, y):
        value = 10
        super().__init__(x, y, value)

    def draw(self, screen):
        x = self.x
        y = self.y

        pygame.draw.rect(screen, colors.RED, [x + 10, y, 20, 10])
        pygame.draw.rect(screen, colors.RED, [x + 5, y + 10, 30, 10])
        pygame.draw.rect(screen, colors.RED, [x, y + 20, 40, 10])
        pygame.draw.rect(screen, colors.RED, [x, y + 30, 5, 10])
        pygame.draw.rect(screen, colors.RED, [x + 10, y + 30, 5, 10])
        pygame.draw.rect(screen, colors.RED, [x + 25, y + 30, 5, 10])
        pygame.draw.rect(screen, colors.RED, [x + 35, y + 30, 5, 10])
        pygame.draw.rect(screen, colors.BLACK, [x + 10, y + 15, 5, 5])
        pygame.draw.rect(screen, colors.BLACK, [x + 25, y + 15, 5, 5])



class UFO(GameObject):

    def __init__(self, x, y):
        self.value = 100

        w = 60
        h = 20
        v_x = -4
        v_y = 0

        super().__init__(x, y, w, h, v_x, v_y)

    def draw(self, screen):
        x = self.x
        y = self.y

        pygame.draw.rect(screen, colors.RED, [x + 25, y, 10, 5])
        pygame.draw.rect(screen, colors.RED, [x + 10 , y + 5, 40, 5])
        pygame.draw.rect(screen, colors.RED, [x, y + 10, 60, 5])
        pygame.draw.rect(screen, colors.RED, [x + 10, y + 15, 40, 5])
