from pyglet.window import Window
from pyglet.window import FPSDisplay
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet.sprite import Sprite
from pyglet import image
import math
import time

class Canvas(Window):
    def __init__(self):
        super().__init__(width=800, height=600)
        self.fps_display = FPSDisplay(self)
        self.batch = Batch()
        self.time_label = Label(x=10, y=580, font_size=16, batch=self.batch)
        self.sprites = [Sprite(image.load(f"{c}.png"), batch=self.batch) for c in "python"]
        self.angle = 0.0
        
    def start(self):
        update_frequency = 1 / 60
        last_time = time.perf_counter()
        while self.angle < 25:
            elapsed_time = time.perf_counter() - last_time
            if elapsed_time > update_frequency:
                last_time = time.perf_counter()
                self.dispatch_events()
                self.on_update(elapsed_time)
                self.on_draw()
                self.flip()
        
    def on_update(self, delta_time):
        self.time_label.text = f"{delta_time:.6f}"
        self.angle += delta_time
        for i, sprite in enumerate(self.sprites):
            sprite.x = math.cos(self.angle - i * 0.5) * 140 + 370
            sprite.y = math.sin(self.angle - i * 0.3) * 140 + 270
        
    def on_draw(self):
        self.clear()
        self.batch.draw()
        self.fps_display.draw()
        
canvas = Canvas()
canvas.start()