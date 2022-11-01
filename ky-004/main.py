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
