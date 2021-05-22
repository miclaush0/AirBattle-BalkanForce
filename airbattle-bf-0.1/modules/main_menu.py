from time import sleep
import pygame
import random
from pygame.display import set_allow_screensaver
from pygame.event import set_allowed
from pygame.surfarray import array_alpha

class MainMenu:
    def __init__(self):
        self.background = pygame.image.load('images\\menu\\background.png')
        self.tree = pygame.image.load('images\\menu\\tree.png')
        self.trees = []
        for y in range(-50, 600, 70):
            for x in range(-50, 800, 70):
                self.trees.append([x + random.randint(50, 70), y + random.randint(50, 70)])
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
            self.update_menu()

        return self.surface

    def update_background(self, dt):
        if self.idx < 30:
            self.alpha_level += 8
        elif self.idx >= 30:
            self.alpha_level = 255
        
        # Background movement
        self.bg_y += 1 * dt
        if int(self.bg_y) == 0:
            self.bg_y = -600

        # Trees movement
        for tree in self.trees:
            tree[1] += 1 * dt
        
        bin = []
        for tree in self.trees:
            if tree[1] >= 650:
               bin.append(tree)

        for tree in bin:
            self.trees.remove(tree)

        if self.bg_y == -600:
            for y in range(-600, -60, 70):
                for x in range(-70, 800, 70):
                    self.trees.append([x + random.randint(50, 70), y + random.randint(50, 70)]) 

        # Update
        self.surface.set_alpha(self.alpha_level)
        self.surface.blit(self.background, [0, self.bg_y])
        for tree in self.trees:
            self.surface.blit(self.tree, tree)

    def update_menu(self):
        if self.selected == 