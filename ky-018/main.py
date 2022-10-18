# Jonathan Mojica
# Micropython

from machine import Pin
from utime import sleep

sensor = Pin(0, Pin.IN)

while True:
    sensor_value = sensor.value()
    if not sensor_value:
        print("Light")
    else:
        print("Dark")
    sleep(0.5)
