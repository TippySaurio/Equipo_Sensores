# ky-016

## Code
```python
# Diaz Rodriguez Jorge Said - 19211629
# Micropython

from machine import Pin
import time

led_pins = [22,26,27]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT),
        Pin(led_pins[2],Pin.OUT)]
delay_t = 0.1
while True:
    leds[0].high()
    leds[1].high()
    leds[2].high()
    time.sleep(1)
    leds[2].low()
    leds[0].high()
    leds[1].high()

```
## Result


 ![](https://media0.giphy.com/media/go8UAXKx6GHRJVtUBL/giphy.gif?cid=790b7611e2bd9ea5226e2a9d00d1896d736dedb60477cfd2&rid=giphy.gif&ct=g)
