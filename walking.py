# -*- coding: utf-8 -*-

import pygame
import state

class Walking(state.State):
    def __init__(self, perso):
        super(Walking, self).__init__(perso)
        self.left_walking_frames = ["left", "left-walking1", "left-walking2"]
        self.right_walking_frames = ["right", "right-walking1", "right-walking2"]
        self.frame = 0
 
    def handle_event(self, event):
        if event.key == pygame.K_a:
            self.perso.direction = "left"
            return self.walk()
        elif event.key == pygame.K_d:
            self.perso.direction = "right"
            return self.walk()
        elif event.key == pygame.K_SPACE:
            if self.perso.direction == "left":
                self.perso.jump_forward = -5
            else:
                self.perso.jump_forward = 5
            return self.jump()
        elif event.key == pygame.K_j:
            return self.run()
        else:
            return self.no_event()          
 
    def no_event(self):
        return self.stand()
 
    def walk(self):
        if self.perso.direction == "left":
            self.perso.rect.move_ip(-self.perso.walking_speed, 0)
            return self.get_frame(self.left_walking_frames)
        else:
            self.perso.rect.move_ip(self.perso.walking_speed, 0)
            return self.get_frame(self.right_walking_frames)
 
    def __str__(self):
        return "walking"
