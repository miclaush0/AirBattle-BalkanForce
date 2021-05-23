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
        self.title_font = pygame.font.Font('fonts\\kongtext.ttf', 55)
        self.subtitle_font = pygame.font.Font('fonts\\kongtext.ttf', 35)
        self.menu_elem_font = pygame.font.Font('fonts\\kongtext.ttf', 30) 
        self.score_font = pygame.font.Font('fonts\\kongtext.ttf', 25)
        self.credits_font = pygame.font.Font('fonts\\kongtext.ttf', 28)
        self.tcredits_font = pygame.font.Font('fonts\\kongtext.ttf', 20)
        self.trees = []
        
        for y in range(0, 600, 20):
            for x in range(-15, 800, 30):
                self.trees.append([x, y])


        self.surface = pygame.Surface([800, 600])
        self.active = 0
        self.selected = 0
        self.idx = 0
        self.bg_y = -600
        self.alpha_level = 0
        

    def update(self, dt, score):
        if self.active == 0:
            self.update_background(dt)
            self.update_menu()
            self.update_score(score)
        elif self.active == 1:
            self.update_background(dt)
            self.update_credits()
            self.update_score(score)

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



        # Update
        self.surface.set_alpha(self.alpha_level)
        self.surface.blit(self.background, [0, self.bg_y])
        for tree in self.trees:
            self.surface.blit(self.tree, tree)

    def update_menu(self):
        self.surface.blit(self.title_font.render('AirBattle', True, [225, 225, 0]), [20, 190])
        self.surface.blit(self.subtitle_font.render('Balkan Force', True, [225, 225, 0]), [22, 248])
        
        if self.selected == 1:
            self.surface.blit(self.menu_elem_font.render('Play', True, [225, 225, 225]), [20, 350])
        else:
            self.surface.blit(self.menu_elem_font.render('Play', True, [225, 225, 0]), [20, 350])
        if self.selected == 2:
            self.surface.blit(self.menu_elem_font.render('Credits', True, [225, 225, 225]), [20, 400])
        else:
            self.surface.blit(self.menu_elem_font.render('Credits', True, [225, 225, 0]), [20, 400])
        if self.selected == 3:
            self.surface.blit(self.menu_elem_font.render('Quit', True, [225, 225, 225]), [20, 450])
        else:
            self.surface.blit(self.menu_elem_font.render('Quit', True, [225, 225, 0]), [20, 450])

    def update_score(self, score):
    
        self.surface.blit(self.score_font.render('Best score:' + score, True, [255, 255, 0]), [440, 500])

    def update_credits(self):
        self.surface.blit(self.title_font.render('AirBattle', True, [225, 225, 0]), [150, 40])
        self.surface.blit(self.subtitle_font.render('Balkan Force', True, [225, 225, 0]), [152, 98])
        
        self.surface.blit(self.credits_font.render('Producers/Designers', True, [225, 225, 0]), [20, 200])
        self.surface.blit(self.tcredits_font.render('Gosman Mihail', True, [225, 225, 10]), [20, 240])
        self.surface.blit(self.tcredits_font.render('Minca Valentin', True, [225, 225, 10]), [20, 265])

        self.surface.blit(self.credits_font.render('Special Thanks', True, [225, 225, 0]), [20, 320])
        self.surface.blit(self.tcredits_font.render('zone38@zone38.net', True, [225, 225, 10]), [20, 360])
        self.surface.blit(self.tcredits_font.render('opengameart.org', True, [225, 225, 0]), [20, 385])