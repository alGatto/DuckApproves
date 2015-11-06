__author__ = 'dylan'

import pygame

black = (0,0,0) # on definit une couleur
pygame.font.init()

class Score():
    """La classe qui affiche le score"""
    def __init__(self, count = 15):
        """on initialise la classe"""
        self.font = pygame.font.SysFont(None, 25)
        """on definit un font pour l'affichage"""
        self.text = self.font.render("Score : "+str(count), True, black)
        """on affiche notre score"""

# ne pas oublier avec la collision d'incementer la valeur count


