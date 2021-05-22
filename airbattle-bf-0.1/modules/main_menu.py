import pygame
import random

from pygame.display import set_allow_screensaver
from pygame.event import set_allowed
from pygame.surfarray import array_alpha
from time import sleep

class MainMenu:
    def __init__(self):
        self.background = pygame.image.load('images\\menu\\background.png')
        self.tree = pygame.image.load('images\\menu\\tree.png')
        self.title = pygame.image.load('images\\menu\\title.png')
        self.play_s = pygame.image.load('images\\menu\\play_s.png')
        self.play = pygame.image.load('images\\menu\\play.png')
        self.credits_s = pygame.image.load('images\\menu\\credits_s.png')
        self.credits = pygame.image.load('images\\menu\\credits.png')
        self.quit_s = pygame.image.load('images\\menu\\quit_s.png')
        self.quit = pygame.image.load('images\\menu\\quit.png')
        self.trees = []
        for y in range(-50, 600, 70):
            for x in range(-50, 800, 70):
                self.trees.append([x + random.randint(50, 90), y + random.randint(50, 70)])
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

        if int(self.bg_y) == -600:
            for y in range(-600, -50, 70):
                for x in range(-70, 800, 70):
                    self.trees.append([x + random.randint(50, 90), y + random.randint(50, 70)]) 

        # Update
        self.surface.set_alpha(self.alpha_level)
        self.surface.blit(self.background, [0, self.bg_y])
        for tree in self.trees:
            self.surface.blit(self.tree, tree)

    def update_menu(self):
        self.surface.blit(self.title, [20, 190])
        
        if self.selected == 1:
            self.surface.blit(self.play_s, [20, 350])
        else:
            self.surface.blit(self.play, [20, 350])
        if self.selected == 2:
            self.surface.blit(self.credits_s, [20, 410])
        else:
            self.surface.blit(self.credits, [20, 410])
        if self.selected == 3:
            self.surface.blit(self.quit_s, [20, 470])
        else:
            self.surface.blit(self.quit, [20, 470])
