import pygame
import random
from pygame import color
from pygame import surface

from pygame.transform import set_smoothscale_backend

def takeSecond(elem):
    return elem[1]

class Game():
    def __init__(self):
        self.background = pygame.image.load('images\\game\\background.png')
        self.tree = pygame.image.load('images\\game\\tree.png')
        self.stats_font = pygame.font.Font('fonts\\kongtext.ttf', 20)
        self.surface = pygame.Surface([800, 600])
        self.active = 0
        self.bg_y = -600
        self.idx = 0
        self.level = 1
        self.alpha_level = 0
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.trees = []
        for i in range(300):
            self.trees.append([random.randint(-15, 800), random.randint(-615, 600)])
        self.trees.sort(key=takeSecond)
        self.player = Player()
        self.bullet = Bullet()
        self.enemy = Enemy()

    
    def update(self, dt):
        if self.active == 0:
            self.update_background(dt)
            self.update_bullet(dt)
            self.update_player()
            self.update_enemy(dt)
            self.update_stats()
            self.collisions()
        elif self.active == 1:
            self.update_pause() 
            
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
        if int(self.bg_y) == -600:
            """for y in range(-615, -15, 50):
                for x in range(-15, 800, 70):
                    self.trees.append([x + random.randint(-40, 20), y + random.randint(0, 10)])"""
            for i in range(300):
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
            self.surface.blit(self.tree, [int(tree[0]), int(tree[1])])    

    def update_player(self):
        self.surface.blit(self.player.image, [self.player.x, self.player.y])

    def update_bullet(self, dt):
        for bullet in self.bullet.bullets:
            self.surface.blit(self.bullet.image, bullet)
        for bullet in self.bullet.bullets:
            bullet[1] += int(-10 * dt)
       
    def update_enemy(self, dt):
        if self.level == 1:
            if len(self.enemy.enemies) <= 10:
                self.enemy.enemies.append([random.randint(10, 730), random.randint(-600, -20)])
        else:
            if len(self.enemy.enemies) <= 15:
                self.enemy.enemies.append([random.randint(10, 730), random.randint(-600, -20)])

        for enemy in self.enemy.enemies:
            if self.level == 1:
                enemy[1] += 1 * dt
            else:
                enemy[1] += 2 * dt

        for enemy in self.enemy.enemies:
            self.surface.blit(self.enemy.image, enemy)

    def update_stats(self):
        self.surface.blit(self.stats_font.render('Score: ' + str(self.score), True, [225, 225, 0]), [20, 20])
        self.surface.blit(self.stats_font.render('Lives: ' + str(self.lives), True, [225, 225, 0]), [20, 50])

# PAUSE !!!
    def update_pause(self):
        if self.game_over:
            surface = pygame.Surface([800, 600])
            surface.fill([255, 255, 255])
            surface.set_alpha(100)
            self.surface.blit(self.background, [0, self.bg_y])
            for enemy in self.enemy.enemies:
                self.surface.blit(self.enemy.image, enemy)
            for bullet in self.bullet.bullets:
                self.surface.blit(self.bullet.image, bullet)
            self.surface.blit(self.player.image, [self.player.x, self.player.y])
            
            if self.game_over:
                self.surface.blit(self.stats_font.render('Game Over', True, [225, 225, 0]), [310, 150])
                self.surface.blit(self.stats_font.render(str(self.score), True, [225, 225, 0]), [380, 200])
                self.surface.blit(self.stats_font.render('Press SPACE to continue...', True, [225, 225, 0]), [190, 250])
        else:
            surface = pygame.Surface([800, 600])
            surface.fill([255, 255, 255])
            surface.set_alpha(100)
            self.surface.blit(self.background, [0, self.bg_y])
            for enemy in self.enemy.enemies:
                self.surface.blit(self.enemy.image, enemy)
            for bullet in self.bullet.bullets:
                self.surface.blit(self.bullet.image, bullet)
            self.surface.blit(self.player.image, [self.player.x, self.player.y])
            
            if self.game_over != True:
                self.surface.blit(self.stats_font.render('Game paused', True, [225, 225, 0]), [20, 150])
                self.surface.blit(self.stats_font.render('<ESC> to continue', True, [225, 225, 0]), [20, 250])
                self.surface.blit(self.stats_font.render('<SPACE> to main menu', True, [225, 225, 0]), [20, 300])
            self.surface.blit(surface, [0, 0])


    def collisions(self):
        for enemy in self.enemy.enemies:
            if enemy[1] >= 670:
                self.enemy.bin.append(enemy)
                self.lives -= 1

        for bullet in self.bullet.bullets:
            if bullet[1] <= -10:
                self.bullet.bin.append(bullet)

        for bullet in self.bullet.bullets:
            for enemy in self.enemy.enemies:
                if bullet[0] >= enemy[0] - 5 and bullet[0] <= enemy[0] + 60:
                    if bullet[1] <= enemy[1] + 60 and bullet[1] >= enemy[1]:
                        self.bullet.bin.append(bullet)
                        self.enemy.bin.append(enemy)
                        self.score += 5
                        
        for enemy in self.enemy.enemies:
            if enemy[1] + 50 >= self.player.y and enemy[1] <= self.player.y + 50:
                if enemy[0] + 55 >= self.player.x and enemy[0] <= self.player.x + 60:
                    self.enemy.bin.append(enemy)
                    self.lives -= 1

        if self.score == 50:
            self.level += 2

        # Delete
        for enemy in self.enemy.bin:
            try: self.enemy.enemies.remove(enemy)
            except: pass
        for bullet in self.bullet.bin:
            try: self.bullet.bullets.remove(bullet)
            except: pass
        self.enemy.bin.clear()    
        self.bullet.bin.clear()

        if self.lives == -1:
            self.game_over = True
            self.active = 1

    def new_game(self):
        self.active = 0
        self.bg_y = -600
        self.idx = 0
        self.alpha_level = 0
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
        self.trees = []
        for i in range(300):
            self.trees.append([random.randint(-15, 800), random.randint(-615, 600)])
        self.trees.sort(key=takeSecond)
        self.player = Player()
        self.bullet = Bullet()
        self.enemy = Enemy()



class Player:
    def __init__(self):
        self.image = pygame.image.load('images\\game\\player.png')
        self.y = 530
        self.x = 370
        self.vel = 5
        

class Bullet:
    def __init__(self):
        self.image = pygame.image.load('images\\game\\bullet.png')
        self.bullets = []
        self.bin = []

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('images\\game\\enemy.png')
        self.enemies = []
        self.vel = 3
        self.bin = []