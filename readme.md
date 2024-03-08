# Custom game loop for smooth animations in Pyglet

The schedule_interval and schedule functions do not call the update function with a steady rate. In this example, you see a custom render loop to calculate delta_time and call update and draw.

![preview](https://github.com/pythonforeveryonetraining/pyglet-custom-loop/blob/main/preview.png)

```
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
```
