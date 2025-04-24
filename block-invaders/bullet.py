import colors
import pygame

from game_object import GameObject


class Bullet(GameObject):

    def __init__(self, x, y):

        w = 6 # make sure w, h is consistent with draw function
        h = 6
        v_x = 0
        v_y = -5
        
        super().__init__(x, y, w, h, v_x, v_y)


    def draw(self, screen):
        x = self.x
        y = self.y
        
        pygame.draw.rect(screen, colors.GREEN, [x, y, 6, 6])
