# -*- coding: utf-8 -*-
__author__ = 'Juliette'
import pygame
import sys
import DuckApprovesGame

pygame.init()

##Définition des couleurs##
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class MenuItem(pygame.font.Font):
    """Classe des items du menu"""
    def __init__(self, text, font=None, font_size=60,
                 font_color=WHITE, pos_x=0, pos_y=0):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class GameMenu():
    def __init__(self, screen, items, functions, bg_color=BLACK, font=None, font_size=30,
                 font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.functions = functions
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)
 
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None

    def set_keyboard_selection(self, key):
        """Marque l'item choisis via les touches haut et bas"""
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Trouve l'item choisi
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                        self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(RED)
 
        # Vérifie si la touche Entrer ou Espace est appuyée
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.functions[text]()
                
    def run(self):
        mainloop = True
        while mainloop:
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
#                    if event.type == pygame.MOUSEBUTTONDOWN:
#                        for item in self.items:
#                            if item.is_mouse_selection(mpos):
#                                self.functions[item.text]()
 
#                if pygame.mouse.get_rel() != (0, 0):
#                    self.mouse_is_visible = True
#                    self.cur_item = None
 
#                self.set_mouse_visibility()
 
            # Redessine le background
            self.screen.fill(self.bg_color)

            for item in self.items:
#               if self.mouse_is_visible:
#                    self.set_mouse_selection(item, mpos)
               self.screen.blit(item.label, item.position)
 
            pygame.display.flip()

if __name__ == "__main__":
    def start():
        print("Démarrer !")
        DuckApprovesGame.App().on_execute()


    def show_rules():
        print("Règles !")

    def show_palmares():
        print("Meilleure score")
 
    # Screen
    screen = pygame.display.set_mode((640, 480), 0, 32)

    menu_items = ('Jouer', 'Palmares', 'Regles','Quit')
    functions = {'Jouer':start,
                'Palmares':show_palmares,
                'Regles':show_rules,
                'Quit': sys.exit}

    pygame.display.set_caption('Duck Approves')
    gm = GameMenu(screen, functions.keys(), functions)
    gm.run()

