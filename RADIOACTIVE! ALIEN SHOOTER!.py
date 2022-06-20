import ppb
from ppb import Scene, keycodes
from ppb.events import KeyPressed, KeyReleased, MouseMotion
from ppb_vector import Vector


class BLP(ppb.Sprite):
    direction = Vector(0, 0)
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
    layer = 2

    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
    
    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == self.up or key_event.key == self.w :
            self.direction += self.mouse_motion-self.position 
        elif key_event.key == self.down or key_event.key == self.s :
            self.direction += self.position-self.mouse_motion
        elif key_event.key == self.shoot :
            key_event.scene.add(c(position = self.position ))
         
        
    def on_key_released(self, key_event: KeyReleased, signal):
        if key_event.key == self.up or key_event.key == self.w :
            self.direction += -self.direction
        elif key_event.key == self.down or key_event.key == self.s :
            self.direction += +self.direction  
          
    def on_mouse_motion(self, mouse_motion: MouseMotion, signal):
       self.mouse_motion = mouse_motion.position 
       self.rotation 

  

class o(ppb.Sprite):
    direction = ppb.Vector(0, 0)
    size = 19
    layer = 1
class c(ppb.Sprite):
    size = 0.5
    direction = ppb.Vector(0, 1)
    speed = 10
    rotation = 90
    layer = 2
    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
        
        

class Alien(ppb.Sprite):
    size = 3
    health = 5
    image = ppb.Image("alien.png")
    layer = 2
    def on_update(self, update_event, signal):

        for bullet in update_event.scene.get(kind=c):
             if (self.position - bullet.position).length < 0.5:  
                self.image  = ppb.Image("remain.png")


def setup(scene):
    scene.add(BLP())
    scene.add(o())    

    for x in [ 8, 1, -1, 3, 4, -4, -5, -6]:
        scene.add(Alien(position=ppb.Vector(x, 8)))
    
ppb.run(setup)

