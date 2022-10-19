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
