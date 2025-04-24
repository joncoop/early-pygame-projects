import colors
import pygame

from game_object import GameObject


class Cannon(GameObject):

    def __init__(self, x, y):

        w = 40  # make sure h, w is consistent with draw function
        h = 30

        super().__init__(x, y, w, h)

    def get_rect(self):
        return [self.x, self.y + 10, self.width, self.height - 10]

    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.rect(screen, colors.BLUE, [x + 18, y, 4, 5])
        pygame.draw.rect(screen, colors.BLUE, [x + 13, y + 5, 14, 5])
        pygame.draw.rect(screen, colors.BLUE, [x, y + 10, 40, 20])


    def draw_icon(self, screen, x, y):
        pygame.draw.rect(screen, colors.BLUE, [x + 18, y, 4, 5])
        pygame.draw.rect(screen, colors.BLUE, [x + 13, y + 5, 14, 5])
        pygame.draw.rect(screen, colors.BLUE, [x, y + 10, 40, 20])
