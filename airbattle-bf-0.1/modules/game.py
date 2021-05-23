import pygame

class Game():
    def __init__(self):
        self.background = pygame.image.load('images\\game\\background.png')
        self.tree = pygame.image.load('images\\game\\tree.png')
        self.surface = pygame.Surface([800, 600])
        self.trees = []

    