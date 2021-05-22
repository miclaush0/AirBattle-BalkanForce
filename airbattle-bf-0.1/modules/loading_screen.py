import pygame

class LoadingScreen:
    def __init__(self):
        self.logo = pygame.image.load('images\\logo.png')
        self.surface = pygame.Surface([800, 600])
        self.idx = 0
        self.alpha_level = 0
        self.active = True

    def update(self):
        self.surface.fill([0, 0, 0])

        if self.idx < 30:
            self.alpha_level += 8
        elif self.idx >= 30 and self.idx < 60:
            self.alpha_level = 255
        elif self.idx >= 60 and self.idx < 90:
            self.alpha_level -= 8
        elif self.idx >= 90 and self.idx < 95:
            self.alpha_level = 0
        else:
            self.active = False

        self.surface.blit(self.logo, [0, 0])
        self.surface.set_alpha(self.alpha_level)
        self.idx += 1
        return self.surface