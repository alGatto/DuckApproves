# -*- coding: utf-8 -*-
__author__ = 'alicia'

import pygame
import perso
import cevent
import plate
import camera
import score
import objects
from random import randint


class App(cevent.Events):
    """App est la classe principale"""
    """App hérite de la classe Events"""
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1024, 683
    def on_init(self):
        """Appel pygame.init() qui initialize tout les modules PyGame"""
        pygame.init()
        
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Duck Approves')
        pygame.mouse.set_visible(1)
        clock = pygame.time.Clock()
        self._running = True
        self._image_background = pygame.image.load("resources/level1back.png").convert()
 
    def on_exit(self):
        self._running = False #La fonction _running est mise à False et donc coupe la boucle de jeu

    def on_loop(self):
        """Calcule les changements dans le jeu (ex: mouvements)"""
        perso.handle_animation()

    def on_render(self):
        """Permet d'afficher les graphiques à l'écran"""
        self._display_surf.blit(self._image_background, (0,0))#Affiche l'image de fond à l'écran
        ##self._display_surf.blit(PERSO._image_player, (x,y))
        self._display_surf.blit(plateform.image, plateform.rect)
        self._display_surf.blit(perso.image, perso.rect, perso.area)
        for i in range(0, 10):
            self._display_surf.blit(plateform.image, (randint(200,1000), randint(500,600)))

        self._display_surf.blit(score.text,(0,0))
        pygame.display.flip()

    def on_cleanup(self):
        """Appel pygame.quit() pour quitter tout les modules PyGame. Rien d'autre ne sera nettoyer par Python."""
        pygame.quit()
        quit()
 

    def on_execute(self):
        """Méthode qui fait marcher le jeu, elle contient la boucle de jeu"""
        if self.on_init() == False: #Initialise pygame
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            perso.handle_event(event)
            #camera.move_camera(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup() #Appel pygame.quit() pour quitter tout les modules PyGame

plateform = plate.World()
perso = perso.Perso((250, 355), plateform)
camera = camera.Camera()
score = score.Score()
obj = objects.Box
