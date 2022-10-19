### KY-034
###      7
### COLOR FLASH
***
## CODIGO
```python
## Instituto Tecnológico de Tijuana
    ##Depto de Sistemas y Computación
    ## Ing. En Sistemas Computacionales
       
    ## Autor : Mondaca Medina Sofia Carolina
    ## Repositorio:  https://github.com/TippySaurio/Equipo_Sensores

import time
from machine import Pin
led = Pin(13,Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

```

## Resultado

<div style="position: relative; padding-bottom: 200%; height: 0;"><iframe src="https://www.loom.com/embed/1c9120fabad44e0aa49ee18bc539559a" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>