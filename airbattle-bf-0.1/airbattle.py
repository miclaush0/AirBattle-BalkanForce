import ctypes
import pygame

from modules.data_handler import *


# Hiding the console 
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


# Constants
WIDTH = 800
HEIGHT = 600


# Graphic window initialization 
pygame.init()
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('AirBattle - Balkan Force')


# Objects initialization
data_handler = DataHandler()
print(data_handler.data)