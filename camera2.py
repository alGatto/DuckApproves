# -*- coding: utf-8 -*-
__author__ = 'alicia'

import pygame
from level import *

class Camera(pygame.Rect):
    """La classe de la caméra sur le joueur"""
    cameraSlackX = 80
    cameraSlackY = 60
    def __init__(self, targetRect, windowWidth, windowHeight):
        super(Camera,self).__init__(targetRect.centerx-(windowWidth/2), 
                                    targetRect.centery-(windowHeight/2), 
                                    windowWidth, windowHeight)
        
    def update(self, rect, level):
        #self.centerx = rect.centerx
        #self.centery = rect.centery
        # determiner si rect est en dehors de la caméra
        if self.centerx - rect.centerx > self.cameraSlackX:
            self.left = rect.centerx + self.cameraSlackX - self.width/2
        elif rect.centerx - self.centerx > self.cameraSlackX:
            self.left = rect.centerx - self.cameraSlackX - self.width/2
        if self.centery - rect.centery > self.cameraSlackY:
            self.top = rect.centery + self.cameraSlackY - self.height/2
        elif rect.centery - self.centery > self.cameraSlackY:
            self.top = rect.centery - self.cameraSlackY - self.height/2
        
        # Garde la caméra dans les frontières du niveau
        if self.right > level.rightEdge - level.blockWidth:
            self.right = level.rightEdge - level.blockWidth
        elif self.left < level.blockWidth:
            self.left = level.blockWidth
        if self.top < level.blockHeight*3:
            self.top = level.blockHeight*3
        elif self.bottom > level.bottomEdge:
            self.bottom = level.bottomEdge
        
        return self