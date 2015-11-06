# -*- coding: utf-8 -*-
__author__ = 'alicia'

import pygame
from random import randint

RLEACCEL = 16384

class Objects(pygame.sprite.Sprite):
    def __init__(self, x, y,color, width, height):

        # Appel la classe parent du constructeur (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.box = pygame.image.load("brick1.png").convert()
        self.box_rect = self.box.get_rect()
        self.x = x
        self.y = y
        self. pos = (x, y)

class Sprite(pygame.sprite.Sprite):
    """ La classe de base pour les sprites """
    def __init__(self, x = 0, y = 0):
        "Initialisation"
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def move_x(self, x):
        self.x = self.x + x
        self._move()

    def move_y(self, y):
        self.y = self.y + y
        self._move()

    def set_x(self, x):
        self.x = x
        self._move()

    def set_y(self, y):
        self.y = y
        self._move()

    def _move(self):
        self.rect.center = (self.x,self.y)


    # Initualisation des images des sprites
    def init_image(self, imgPath):
        self.image = pygame.image.load(imgPath).convert()
        self.image.set_colorkey(self.image.get_at((0,0)), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)



class Monster(Sprite):
    def __init__(self, x,y):
        Sprite.__init__(self,x,y)
        self.init_image('brick1.png')

    def move(self):
        self.move_x(randint(-5, 5))
        self.move_y(randint(-5, 5))

    def draw(self):
        if self.perso.life <= 1:
            # crée  un ennemi
            if self.monster == None:
                case = randint(5 ,1000)
                if case > 0:
                    self.monster = Monster(randint(0, 1024), randint(-50, 50))
                    self.allsprites.add(self.monster)
                    self.monster.move()
            else:
                self.monster.move()
                # toucher l'ennemi
                if self.perso.rect.colliderect(self.monster.rect):
                    self.perso.life = self.perso.life - 1

class Box(Sprite):
    def __init__(self):
        self.img = pygame.image.load("brick1.png").convert()
        self.obj_pos = (300, 600)

