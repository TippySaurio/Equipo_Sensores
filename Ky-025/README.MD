# ky-025

## Code

```python
# Diaz Rodriguez Jorge Said 19211629
# MicroPhyton

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
