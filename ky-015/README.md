```
# Jonathan Mojica
# Micropython

# Controlar tiempos y para trabajar con el sensor, respectivamente
from machine import Pin, I2C
from time import sleep
from dht import  DHT11

# Declarando que vamos a usar el Pin de nuestro RPI
pin = Pin(0)
sensor = DHT11(pin)

while True:
    print('------------------')
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    
    # Este codigo es para imprimir en la pantalla
    #print("Temperatura: " + str(T) + chr (0xDF) + "C")
    
    #print("Humedad: "+ str(H) +"%")
    sleep(2)    
    ```
![]("./ky-015.gif")
