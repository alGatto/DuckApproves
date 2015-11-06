# -*- coding: utf-8 -*-
__author__ = 'alicia'


import pygame

class Camera:
    def __init__(self):
        self.posX = 0
        self.posY = 0

    def move_camera(self, event):
        if event.key == pygame.K_a:
            self.posX = self.posX - 5
        elif event.key == pygame.K_d:
            self.posX = self.posX + 5
        elif event.key == pygame.K_SPACE:
            self.posY = self.posY - 5

