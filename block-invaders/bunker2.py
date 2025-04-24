import colors
import pygame

from game_object import GameObject


class Bunker(GameObject):

    def __init__(self, x, y):

        w = 80 # make sure h, w is consistent with draw function
        h = 40
        v_x = 0
        v_y = 0
        
        super().__init__(x, y, w, h, v_x, v_y)

    def get_rect(self):
        return [self.x, self.y + 10, self.width, 20]

    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.rect(screen, colors.WHITE, [x + 20, y, 40, 10])
        pygame.draw.rect(screen, colors.WHITE, [x, y + 10, 80, 20])
        pygame.draw.rect(screen, colors.WHITE, [x, y + 30, 20, 10])
        pygame.draw.rect(screen, colors.WHITE, [x + 60, y + 30, 20, 10])
