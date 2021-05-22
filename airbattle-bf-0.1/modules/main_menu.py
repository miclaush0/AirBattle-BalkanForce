import pygame
from pygame.display import set_allow_screensaver
from pygame.event import set_allowed
from pygame.surfarray import array_alpha

class MainMenu:
    def __init__(self):
        self.background = pygame.image.load('images\\menu\\background.png')
        self.tree = pygame.image.load('images\\menu\\tree.png')
        self.trees = []
        for 
        self.surface = pygame.Surface([800, 600])
        self.active = 0
        self.selected = 0
        self.idx = 0
        self.bg_y = -600
        self.alpha_level = 0

    def update(self, dt):
        self.surface.fill([0, 0, 0])
        if self.active == 0:
            self.update_background(dt)

        return self.surface

    def update_background(self, dt):
        if self.idx < 30:
            self.alpha_level += 8
        elif self.idx >= 30:
            self.alpha_level = 255
        
        # Background movement
        self.bg_y += 1 * dt
        if self.bg_y >= 0:
            self.bg_y = -600

        # Trees movement
        for tree in self.trees:
            tree[1] += 1 * dt

        # Update
        self.surface.set_alpha(self.alpha_level)
        self.surface.blit(self.background, [0, self.bg_y])
        for tree in self.trees:
            self.surface.blit(self.tree, tree)
