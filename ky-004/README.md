### KY-004
### BUTTON
***
## CODIGO
```python
## Instituto Tecnológico de Tijuana
    ##Depto de Sistemas y Computación
    ## Ing. En Sistemas Computacionales
       
    ## Autor : Mondaca Medina Sofia Carolina
    ## Repositorio:  https://github.com/TippySaurio/Equipo_Sensores

from time import sleep_ms
from machine import Pin
button = Pin(17,Pin.IN)
led = Pin(25, Pin.OUT)

while True:
  
    if button.value()==1:
        print("Se encendio el led")
    sleep_ms(200)

```

## Resultado

<a href="https://www.loom.com/share/e85c0a6b864a46a0ab0d9fe2ef6ad565">
    <p>KY-004 BUTTON - Watch Video</p>
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/e85c0a6b864a46a0ab0d9fe2ef6ad565-with-play.gif">
  </a>
