import pygame
import random
from pygame.transform import set_smoothscale_backend

def takeSecond(elem):
    return elem[1]

class Game():
    def __init__(self):
        self.background = pygame.image.load('images\\game\\background.png')
        self.tree = pygame.image.load('images\\game\\tree.png')
        self.surface = pygame.Surface([800, 600])
        self.active = 0
        self.bg_y = -600
        self.idx = 0
        self.alpha_level = 0
        self.trees = []
        for i in range(300):
            self.trees.append([random.randint(-15, 800), random.randint(-615, 600)])
        self.trees.sort(key=takeSecond)
    
    def update(self, dt):
        if self.active == 0:
            self.update_background(dt)
        elif self.active == 1:
            pass
            
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
        print(self.bg_y)
        # Trees movement
        if int(self.bg_y) == -600:
            """for y in range(-615, -15, 50):
                for x in range(-15, 800, 70):
                    self.trees.append([x + random.randint(-40, 20), y + random.randint(0, 10)])"""
            for i in range(200):
                self.trees.append([random.randint(-15, 800), random.randint(-615, -15)])
            self.trees.sort(key=takeSecond)
        
        for tree in self.trees:
            tree[1] += 1 * dt
        
        bin = []
        for tree in self.trees:
            if tree[1] >= 650:
               bin.append(tree)

        for tree in bin:
            self.trees.remove(tree)

        
        self.surface.set_alpha(self.alpha_level)
        self.surface.blit(self.background, [0, int(self.bg_y)])
        for tree in self.trees:
            self.surface.blit(self.tree, tree)    