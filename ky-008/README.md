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

<div style="position: relative; padding-bottom: NaN%; height: 0;"><iframe src="https://www.loom.com/embed/0ed28becb91c4f269a045007220664d8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
