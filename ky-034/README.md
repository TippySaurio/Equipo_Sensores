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

<a href="https://www.loom.com/share/1c9120fabad44e0aa49ee18bc539559a">
    <p>Android recording - 18 oct 2022 - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/1c9120fabad44e0aa49ee18bc539559a-with-play.gif">
  </a>
