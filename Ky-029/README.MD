# ky-029

## Code
```python
#Diaz Rodriguez Jorge Said 19211629
# MicroPython

from machine import Pin
import time

led_pins = [22,26]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.1
while True:
        leds[0].high()
        time.sleep(1)
        leds[0].low()
        leds[1].high()
        time.sleep(0.75)
    
```
## Result
![]()
https://www.loom.com/share/3c9f336f88a34fe8b5593805d47ba547
