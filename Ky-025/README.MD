# ky-025

## Code

```python
# Diaz Rodriguez Jorge Said 19211629
# MicroPython

from machine import Pin,ADC
from time import sleep

pins = ADC(Pin(34))

while True:
	if pins.read_u16() =< 32000 :
		print("Si hay campo magnetico")
	else:
		print("No hay campo magnetico")
	time.sleep(1)
    
```
## Result
![]()
https://www.loom.com/share/2c441c45fe014d6484a46b35f1c25449
