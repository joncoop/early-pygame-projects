import colors
import pygame
import random


class Ground:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, colors.GREY, [self.x, self.y, self.w, self.h])


class Stars:

    def __init__(self, x, y, w, h, num_stars):
        self.stars = []

        for n in range(num_stars):
            a = random.randrange(x, x + w)
            b = random.randrange(y, y + h)

            self.stars.append([a, b])

    def draw(self, screen):
        for s in self.stars:
            pygame.draw.ellipse(screen, colors.WHITE, [s[0], s[1], 2, 2])


class Mountains:

    def __init__(self, x, y, w, h, num_peaks):
        self.peaks = []

        self.peaks.append([x, y + h])
        self.peaks.append([x, y + 4 * h // 5])

        for n in range(1, num_peaks):
            center = n * w // num_peaks
            offset = w // num_peaks // 4

            a = random.randrange(center - offset, center + offset)
            b = random.randrange(y, y + 4 * h // 5)

            self.peaks.append([a, b])

        self.peaks.append([x + w, y + 4 * h // 5])
        self.peaks.append([x + w, y + h])


    def draw(self, screen):
        pygame.draw.polygon(screen, colors.LIGHT_GREY, self.peaks)
