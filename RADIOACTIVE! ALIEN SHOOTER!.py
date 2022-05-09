from re import X
from this import d
from tkinter import W
from turtle import position
import ppb
from ppb import keycodes
from ppb.events import KeyPressed, KeyReleased
from ppb_vector import Vector


class BLP(ppb.Sprite):
    direction = ppb.Vector(0, 0)
    size = 3
    speed = 6
    position = ppb.Vector(0, -7)
    left = keycodes.Left 
    right = keycodes.Right 
    shoot = keycodes.Space
    d = keycodes.D
    s = keycodes.S
    a = keycodes.A
    w = keycodes.W
    up = keycodes.Up
    down = keycodes.Down
    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
    
    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == self.left or key_event.key == self.a :
            self.direction += ppb.Vector(-1, 0) 
        elif key_event.key == self.right or key_event.key ==  self.d :
            self.direction += ppb.Vector(1, 0)
        elif key_event.key == self.up or key_event.key == self.w :
            self.direction += ppb.Vector(0,1 )
        elif key_event.key == self.down or key_event.key == self.s :
            self.direction += ppb.Vector(0, -1 )
        elif key_event.key == self.shoot :
            key_event.scene.add(c(position = self.position ))
              
    def on_key_released(self, key_event: KeyReleased, signal):
        if key_event.key == self.left or key_event.key == self.a :
            self.direction += ppb.Vector(1, 0) 
        elif key_event.key == self.right or key_event.key == self.d :
            self.direction += ppb.Vector(-1, 0)
        elif key_event.key == self.up or key_event.key == self.w :
            self.direction += ppb.Vector(0,-1 )
        elif key_event.key == self.down or key_event.key == self.s :
            self.direction += ppb.Vector(0, 1 )

class o(ppb.Sprite):
    direction = ppb.Vector(0, 0)
    size = 19

class c(ppb.Sprite):
    size = 0.5
    direction = ppb.Vector(0, 1)
    speed = 10
    rotation = 90
    
    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
        
        

class Alien(ppb.Sprite):
    size = 3
    health = 5
    def on_update(self, update_event, signal):

        for bullet in update_event.scene.get(kind=c):
             if (self.position - bullet.position).length < 0.87567859066504398276254567348950498372652637485905948736:  
                 update_event.scene.remove(self)


def setup(scene):
    scene.add(BLP())
    
    
    
    for x in [ 8, 1, -1, 3, 4, -4, -5, -6]:
        scene.add(Alien(position=ppb.Vector(x, 8)))
    
ppb.run(setup)
        
#for x in [ 0]:
    #scene.add(o(position=ppb.Vector(x, 0)))