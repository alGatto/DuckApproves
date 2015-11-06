# -*- coding: utf-8 -*-
__author__ = 'alicia'


class State(object):
    """This is the template for all the other states"""
 
    def __init__(self, perso):
        self.perso = perso
 
    def jump(self):
        print("Jump")
        self.perso.state = self.perso.jumping_state
        return self.perso.state.jump()  
 
    def fall(self):
        self.perso.state = self.perso.falling_state
        return self.perso.state.fall()
 
    def walk(self):
        self.perso.state = self.perso.walking_state
        return self.perso.state.walk()
 
    def run(self):
        self.perso.state = self.perso.running_state
        return self.perso.state.run()
 
    def stand(self):
        self.perso.state = self.perso.standing_state
        return self.perso.state.stand()
 
    def get_frame(self, frame_set):
        self.frame += 1
 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
 
        return frame_set[self.frame]            
 
    def __str__(self):
        return "Default state"
