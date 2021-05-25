import ctypes
from typing import AsyncIterable
import pygame
import time

from pygame.constants import K_w
from pygame.display import get_active

from modules.data_handler import *
from modules.loading_screen import *
from modules.main_menu import *
from modules.game import *


# Hiding the console 
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0 )


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
game = Game()

# Globals initialization
clock = pygame.time.Clock()


# Main function
def main():
    click = soun_obj=pygame.mixer.Sound("sounds\\click.wav")
    shoot = soun_obj=pygame.mixer.Sound("sounds\\shoot.wav")
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
    pressed_enter = False
    pressed_escape = False

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
            window.blit(main_menu.update(dt, data_handler.data[1]), [0, 0])
        elif active == 2:
            window.blit(game.update(dt), [0, 0])

        pygame.display.update()

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or
                    event.key == pygame.K_w):
                    pressed_up = True
                elif (event.key == pygame.K_DOWN or
                    event.key == pygame.K_s):
                    pressed_down = True
                elif (event.key == pygame.K_LEFT or
                    event.key == pygame.K_a):
                    pressed_left = True
                elif (event.key == pygame.K_RIGHT or
                    event.key == pygame.K_d):
                    pressed_right = True
                elif (event.key == pygame.K_RETURN or
                    event.key == pygame.K_SPACE):
                    pressed_enter = True 
                elif event.key == pygame.K_ESCAPE:
                    pressed_escape = True          

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP or
                    event.key == pygame.K_w):
                    pressed_up = False
                elif (event.key == pygame.K_DOWN or
                    event.key == pygame.K_s):
                    pressed_down = False
                elif (event.key == pygame.K_LEFT or
                    event.key == pygame.K_a):
                    pressed_left = False
                elif (event.key == pygame.K_RIGHT or
                    event.key == pygame.K_d):
                    pressed_right = False
                elif (event.key == pygame.K_RETURN or
                    event.key == pygame.K_SPACE):
                    pressed_enter = False         

        #Logic
        if active == 0:
            pass
        
        elif active == 1:
            if pressed_down:
                pressed_down = False
                click.play()
                if main_menu.selected != 3:
                    main_menu.selected += 1
                else:
                    main_menu.selected = 1
            elif pressed_up:
                pressed_up = False
                click.play()
                if main_menu.selected != 1:
                    main_menu.selected -= 1
                else:
                    main_menu.selected = 3
            elif pressed_enter:
                pressed_enter = False
                click.play()
                if main_menu.selected == 1:
                    game.new_game()
                    active = 2
                elif main_menu.selected == 2:
                    if main_menu.active == 0:
                        main_menu.active = 1
                    else:
                        main_menu.active = 0
                elif main_menu.selected == 3:
                    running = False

        elif active == 2:
            if game.active == 0:
                if pressed_left:
                    if game.player.x - game.player.vel >= 0:
                        game.player.vel += 3
                        game.player.x += -game.player.vel * dt  
                    else:
                        game.player.vel = 0
                        game.player.x = 0
                elif pressed_right:
                    if game.player.x + game.player.vel <= WIDTH - 60:
                        game.player.vel += 4
                        game.player.x += game.player.vel * dt
                    else:
                        game.player.x = WIDTH - 60
                        game.player.vel = 10
                elif pressed_enter:
                    game.bullet.bullets.append([game.player.x + 24, game.player.y])
                    shoot.play()
                    pressed_enter = False       
                elif pressed_escape:
                    pressed_escape = False
                    game.active = 1
                else:
                    game.player.vel = 10
            elif game.active == 1:
                if game.game_over == True:
                    if pressed_enter:
                        if game.score > int(data_handler.data[1]):
                            data_handler.data[1] = str(game.score)
                            data_handler.write_data()
                        active = 1
                        pressed_enter = False
                else:
                    if pressed_escape:
                        game.active = 0
                        pressed_escape = False
                    elif pressed_enter:
                        if game.score > int(data_handler.data[1]):
                            data_handler.data[1] = str(game.score)
                            data_handler.write_data()
                        
                        active = 1
                        pressed_enter = False

    pygame.quit()
    exit()
            

# Starting the main function
main()