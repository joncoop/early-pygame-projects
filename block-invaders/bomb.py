import colors
import pygame

from game_object import GameObject


class Bomb(GameObject):

    def __init__(self, x, y):

        w = 4 # make sure h, w is consistent with draw function
        h = 8
        v_x = 0
        v_y = 3
        
        super().__init__(x, y, w, h, v_x, v_y)


    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.rect(screen, colors.BLUE, [x, y, 4, 8])
