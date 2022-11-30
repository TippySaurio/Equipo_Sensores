# ky-021

## Code

```python

# Diaz Rodriguez Jorge Said 19211629
# MicroPython

from machine import Pin
import time

pins = Pin(17,Pin.IN)


led_pins = [2,3,4]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT),
        Pin(led_pins[2],Pin.OUT)]

while True:
    if pins.value() == False:
        print("Si hay campo magnetico")
        leds[0].high()
        leds[1].high()
        leds[2].high()
    else:
        print("No hay campo magnetico")
        leds[0].low()
        leds[1].low()
        leds[2].low()
    time.sleep(1)
    
```

## Result

![]()
https://www.loom.com/share/2c441c45fe014d6484a46b35f1c25449
