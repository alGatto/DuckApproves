# -*- coding: utf-8 -*-
__author__ = 'alicia'

import pygame

class Level(object):
    """La classe du niveau """
    blank = '.'
    block = '0'
    blockWidth = 75
    blockHeight = 75
    
    def __init__(self, file):
        #Lire le fichier du niveau pour les collisions"""
        self.collisionLayer = [row.strip('\n') for row in\
                          open(file, 'r').readlines()]
        self.levelWidth = len(self.collisionLayer[0])
        self.levelHeight = len(self.collisionLayer)
        
        self.leftEdge = 0
        self.topEdge = 0
        self.rightEdge = self.levelWidth * self.blockWidth
        self.bottomEdge = self.levelHeight * self.blockHeight
        
        
        self.blockSurf = pygame.Surface((self.blockWidth, self.blockHeight))
        self.blockSurf.fill((255,255,255))