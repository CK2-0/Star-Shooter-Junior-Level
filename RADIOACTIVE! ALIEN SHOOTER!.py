import ppb
from ppb import Scene, keycodes
from ppb.events import KeyPressed, KeyReleased, MouseMotion
from ppb_vector import Vector
import ppb
from ppb import keycodes
from ppb.events import KeyPressed
from ppb.features import loadingscene
import math
class Rocket(ppb.Sprite):
    direction = Vector(0, 0)
    size = 2.5
    speed = 0
    position = ppb.Vector(0, -7)
    shoot = keycodes.Space
    s = keycodes.S
    w = keycodes.W
    up = keycodes.Up
    down = keycodes.Down
    layer = 3
    image = ppb.Image("Level1Rocket.png")
    mouse_position = ppb.Vector(0, -7)
    
    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        rotation_direction = self.mouse_position - self.position 
        self.position += rotation_direction * self.speed * update_event.time_delta  
        self.rotation = ( math.degrees(math.atan2( rotation_direction.y, rotation_direction.x)) + 32)
          
        
    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == self.up or key_event.key == self.w :
            self.speed += 3
        elif key_event.key == self.down or key_event.key == self.s :
            self.speed += -1
        elif key_event.key == self.shoot :
            key_event.scene.add(Bullet(position = self.position, direction= self.mouse_position - self.position, rotation= self.rotation - 30))
 
         
        
    def on_key_released(self, key_event: KeyReleased, signal):
        if key_event.key == self.up or key_event.key == self.w :
            self.speed -= 3
        elif key_event.key == self.down or key_event.key == self.s :
            self.speed -= -1
          
    def on_mouse_motion(self, mouse_motion: MouseMotion, signal):
       self.mouse_position = mouse_motion.position 
       

class o(ppb.Sprite):
    direction = ppb.Vector(0, 0)
    size = 19
    layer = 1
class Bullet(ppb.Sprite):
    size = 0.35
    direction = ppb.Vector(0, 1)
    speed = 15
    image = ppb.Image("l1bullet.png")
    rotation = 90
    layer = 2
    def on_update(self, update_event, signal):
        if self.direction.x and self.direction.y:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
        
class blood(ppb.Sprite):
    size = 4.5
    layer = 2

class Alien(ppb.Sprite):
    size = 2.5
    image = ppb.Image("alien.png")
    layer = 2
    def on_update(self, update_event, signal):

        for bullet in update_event.scene.get(kind=Bullet):
             if (self.position - bullet.position).length < 1:  
                self.image  = ppb.Image("blood.png")


class Label(ppb.Sprite):
    size = 2
    layer = 2
    color = (255, 255, 255)
    text = None
    image = None

    def on_update(self, update_event, signal):
        self.image = ppb.Text(
            self.text,
            font=ppb.Font("ubuntu_font/UbuntuMono-B.ttf", size=40),
            color=self.color,
        )

class LoadingSprite(ppb.Sprite):
    ready_image = ppb.Image("load_bar/center_filled.png")
    waiting_image = ppb.Image("load_bar/center_empty.png")
    layer = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = self.waiting_image


class Level1(ppb.Scene):
    # scene = 

    def on_scene_started(self, scene_started: ppb.events.SceneStarted, signal):
        self.add(Rocket())
        self.add(o())
        for x in [ 8, 1, -1, 3, 4, -4, -5, -6]:
                self.add(Alien(position=ppb.Vector(x, 8)))

    

class Level1Title(ppb.Scene):
    next_scene = Level1

    def on_scene_started(self, scene_started: ppb.events.SceneStarted, signal):
        self.add(Label(text="Level 1"))
        self.add(o())
        


    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == keycodes.Space:
            signal(ppb.events.ReplaceScene(new_scene=self.next_scene))
            signal(ppb.events.StopScene(scene=self))


class LoadScreen(loadingscene.BaseLoadingScene):
    next_scene = Level1Title

    def on_scene_started(self, scene_started: ppb.events.SceneStarted, signal):
        self.add(o())

    def get_progress_sprites(self):
        left = LoadingSprite(
            position=ppb.Vector(-4, 0),
            ready_image=ppb.Image("load_bar/left_filled.png"),
            waiting_image=ppb.Image("load_bar/left_empty.png"),
        )
        center = [
            LoadingSprite(position=ppb.Vector(x, 0)) for x in range(-3, 4)
        ]
        right = LoadingSprite(
            position=ppb.Vector(4, 0),
            ready_image=ppb.Image("load_bar/right_filled.png"),
            waiting_image=ppb.Image("load_bar/right_empty.png"),
        )
        return [left, *center, right]

    def update_progress(self, progress):
        bar = sorted(self.get(tag="progress"), key=lambda s: s.position.x)

        progress_index = progress * len(bar)

        for i, sprite in enumerate(bar):
            if i <= progress_index:
                sprite.image = sprite.ready_image
            else:
                sprite.image = sprite.waiting_image


ppb.run(starting_scene=LoadScreen, title="Alien Shooter")

   

    


