# ky-009

## Code
```python
#Diaz Rodriguez Jorge Said 19211629
# MicroPhyton

from machine import Pin
import time

led_pins = [22,26,27]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT),
        Pin(led_pins[2],Pin.OUT)]
delay_t = 0.1
while True:
      for led in leds:
        led.high()
        time.sleep(delay_t)
        led.low() 
        time.sleep(delay_t)
    
```
## Result
![](https://media0.giphy.com/media/go8UAXKx6GHRJVtUBL/giphy.gif?cid=790b7611e2bd9ea5226e2a9d00d1896d736dedb60477cfd2&rid=giphy.gif&ct=g)
