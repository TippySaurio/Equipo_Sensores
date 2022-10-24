### KY-008
### LASER EMIT
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
laser = Pin(17,Pin.OUT)

while True:
    laser.on()
    time.sleep(0.5)
    laser.off()
    time.sleep(0.5)

```

## Resultado

<a href="https://www.loom.com/share/0ed28becb91c4f269a045007220664d8">
    <p>Android recording - 19 oct 2022 - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0ed28becb91c4f269a045007220664d8-with-play.gif">
  </a>
