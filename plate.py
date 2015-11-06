# -*- coding: utf-8 -*-
__author__ = 'alicia'

import pygame

class World(object):
    def __init__(self):
        pygame.display.init()
        width = 1024
        height = 683
        self.screen = pygame.display.set_mode((width, height))
        self.image = pygame.image.load("brick1.png").convert()
        self.rect = self.image.get_rect()
        self.pos=[400,600]
 
        self.solids = [[-10, 3000, 600], [300, 10, 600], [70, 149, 164], [119, 216, 116], [259, 336, 132]]



        
