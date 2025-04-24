import colors
import intersects
import pygame

from game_object import GameObject


class Bunker(GameObject):

    def __init__(self, x, y):

        w = 80  # make sure h, w is consistent with draw function
        h = 40
        v_x = 0
        v_y = 0

        self.bits = []

        b1 = [x + 20, y, 10, 10]
        b2 = [x + 30, y, 10, 10]
        b3 = [x + 40, y, 10, 10]
        b4 = [x + 50, y, 10, 10]

        b5 = [x, y + 10, 10, 10]
        b6 = [x + 10, y + 10, 10, 10]
        b7 = [x + 20, y + 10, 10, 10]
        b8 = [x + 30, y + 10, 10, 10]
        b9 = [x + 40, y + 10, 10, 10]
        b10 = [x + 50, y + 10, 10, 10]
        b11 = [x + 60, y + 10, 10, 10]
        b12 = [x + 70, y + 10, 10, 10]

        b13 = [x, y + 20, 10, 10]
        b14 = [x + 10, y + 20, 10, 10]
        b15 = [x + 20, y + 20, 10, 10]
        b16 = [x + 30, y + 20, 10, 10]
        b17 = [x + 40, y + 20, 10, 10]
        b18 = [x + 50, y + 20, 10, 10]
        b19 = [x + 60, y + 20, 10, 10]
        b20 = [x + 70, y + 20, 10, 10]

        b21 = [x, y + 30, 10, 10]
        b22 = [x + 10, y + 30, 10, 10]
        b23 = [x + 60, y + 30, 10, 10]
        b24 = [x + 70, y + 30, 10, 10]

        self.bits = [b1, b2, b3, b4,
                     b5,  b6, b7, b8, b9, b10, b11, b12,
                     b13, b14, b15, b16, b17, b18, b19, b20,
                     b21, b22, b23, b24]

        super().__init__(x, y, w, h, v_x, v_y)

    def clear_bunker_bits(self, rect):
        bits_to_remove = []
        hit = False

        for b in self.bits:
            if intersects.rect_rect(b, rect):
                bits_to_remove.append(b)
                hit = True

        self.bits = [b for b in self.bits if b not in bits_to_remove]

        return hit

    def draw(self, screen):
        for b in self.bits:
            pygame.draw.rect(screen, colors.WHITE, b)
