# ky-009

## Code

```python
#Diaz Rodriguez Jorge Said 19211629
# MicroPhyton

from machine import Pin
import time

led_pins = [22,26]
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.1
while True:
    for led in leds:
        led.high()
        time.sleep(delay_t)
        led.low() 
        time.sleep(delay_t)
    
```
## Result
![]()
