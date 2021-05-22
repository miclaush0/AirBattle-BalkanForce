import ctypes
import pygame
import time

from modules.data_handler import *
from modules.loading_screen import *
from modules.main_menu import *


# Hiding the console 
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


# Constants
WIDTH = 800
HEIGHT = 600
FPS = 30


# Graphic window initialization 
pygame.init()
pygame.display.set_caption('AirBattle - Balkan Force')
window = pygame.display.set_mode([WIDTH, HEIGHT])


# Objects initialization
data_handler = DataHandler()
loading_screen = LoadingScreen()
main_menu = MainMenu()

# Globals initialization
clock = pygame.time.Clock()


# Main function
def main():
    MessageBox = ctypes.windll.user32.MessageBoxW
    if data_handler.data[0] == 'False':
        res = MessageBox(None, 'This product is distributed under the GPL-3 license.'
                                ' By clicking the OK button, you agree to the terms '
                                'and conditions of the license.'
                                '\nYou can find a copy of the LICENSE.txt file in the product'
                                ' folder.',
                                'Acceptance of the license agreement.', 1)
    
        if res == 1:
            data_handler.data[0] = 'True'
            data_handler.write_data()
        else:
            res = MessageBox(None, 'In order to have access to the program'
                                   ', you must agree to the terms and conditions!',
                                   'Acceptance of the license agreement.', 1)

            if res == 1:
                data_handler.data[0] = 'True'
                data_handler.write_data()
            else:
                pygame.quit()
                exit()

    running = True
    active = 0
    pressed_right = False
    pressed_left = False
    pressed_up = False
    pressed_down = False
    last_time = time.time()

    # main loop
    while running:
        # Framerate independence
        dt = time.time() - last_time
        dt *= FPS
        last_time = time.time()
        clock.tick(FPS)  

        # Graphics
        window.fill([0, 0, 0])
        if active == 0:
            window.blit(loading_screen.update(), [0, 0])
            if loading_screen.active == False:
                active = 1
        elif active == 1:
            window.blit(main_menu.update(dt), [0, 0])
        pygame.display.update()

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

# Starting the main function
main()