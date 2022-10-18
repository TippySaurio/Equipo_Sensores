# Jonathan Mojica
# Micropython

from machine import Pin
from utime import sleep

sensor = Pin(0, Pin.IN)

while True:
    sensor_value = sensor.value()
    if sensor_value:
        print("Sensor straight")
    else:
        print("Sensor tilted")
    sleep(0.5)
