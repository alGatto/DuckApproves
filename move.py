# -*- coding: utf-8 -*-

__author__ = 'alicia'

import pygame
import state



class Standing(state.State):
    def __init__(self, perso):
        super(Standing, self).__init__(perso)
        self.left_stand = "left"
        self.right_stand = "right"
 
    def handle_event(self, event):
        if event.key == pygame.K_a:
            self.perso.direction = "left"
            return self.walk()
        elif event.key == pygame.K_d:
            self.perso.direction = "right"
            return self.walk()
        elif event.key == pygame.K_SPACE:
            return self.jump()
        elif event.key == pygame.K_j:
            return self.run()
        else:
            return self.no_event()
 
    def no_event(self):
        return self.stand()
 
    def stand(self):
        if self.perso.direction == "left":
            return self.left_stand
        else:
            return self.right_stand
 
    def __str__(self):
        return "standing"

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

class Running(state.State):
    def __init__(self, perso):
        super(Running, self).__init__(perso)
        self.left_running_frames = ["left-run1", "left-run2", "left-run3"]
        self.right_running_frames = ["right-run1", "right-run2", "right-run3"]
        self.frame = 0
 
    def handle_event(self, event):
        if event.key == pygame.K_a:
            self.perso.direction = "left"
            return self.run()
        elif event.key == pygame.K_d:
            self.perso.direction = "right"
            return self.run()
        elif event.key == pygame.K_SPACE:
            if self.perso.direction == "left":
                self.perso.jump_forward = -8
            else:
                self.perso.jump_forward = 8
            return self.jump()
        elif event.key == pygame.K_j:
            return self.run()
        else:
            return self.no_event()  
 
    def no_event(self):
        return self.walk()  
 
    def run(self):
        if self.perso.direction == "left":
            self.perso.rect.move_ip(-self.perso.running_speed, 0)
            return self.get_frame(self.left_running_frames)
        else:
            self.perso.rect.move_ip(self.perso.running_speed, 0)
            return self.get_frame(self.right_running_frames)
 
    def __str__(self):
        return "running"

class Jumping(state.State):
    def __init__(self, perso):
        super(Jumping, self).__init__(perso)
        self.left_jump = "left-jump"
        self.right_jump = "right-jump"
 
    def handle_event(self, event):
        if event.key == pygame.K_a:
            self.perso.jump_forward = 0
            self.perso.rect.move_ip(-self.perso.jump_air_power, 0)
        elif event.key == pygame.K_d:
            self.perso.jump_forward = 0
            self.perso.rect.move_ip(self.perso.jump_air_power, 0)
        return self.jump()  
 
    def no_event(self):
        return self.jump()
 
    def jump(self):
        self.perso.jump_frame += 1
        self.perso.rect.move_ip(self.perso.jump_forward, -self.perso.jump_speed)
 
        if self.perso.jump_frame > self.perso.jump_stop_frame:
            if self.perso.jump_forward != 0:
                if self.perso.direction == "left":
                    self.perso.jump_forward = -4
                else:
                    self.perso.jump_forward = 4
            return self.fall()          
 
        if self.perso.direction == "left" :
            return self.left_jump
        else:
            return self.right_jump
 
    def __str__(self):
        return "jumping"

class Falling(state.State):
    def __init__(self, perso):
        super(Falling, self).__init__(perso)
        self.left_fall = "left-fall"
        self.right_fall = "right-fall"
 
    def handle_event(self, event):
        if event.key == pygame.K_a:
            self.perso.jump_forward = 0
            self.perso.rect.move_ip(-self.perso.jump_air_power, 0)
        elif event.key == pygame.K_d:
            self.perso.jump_forward = 0
            self.perso.rect.move_ip(self.perso.jump_air_power, 0)   
        return self.fall()
 
    def no_event(self):
        return self.fall()
 
    def fall(self):
        self.perso.rect.move_ip(self.perso.jump_forward, self.perso.fall_speed)
 
        if not self.perso.check_if_falling():
            self.perso.jump_frame = 0
            self.perso.jump_forward = 0
            return self.stand()
 
        if self.perso.direction == "left":
            return self.left_fall
        else:
            return self.right_fall  
 
    def __str__(self):
        return "falling"
