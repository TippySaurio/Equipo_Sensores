#KY - 026 J. BUSTAMANTE

from machine import Pin
import utime

flame_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Detección de flama")
       utime.sleep(3)
   else:
       print("No Flama")
       utime.sleep(1)
utime.sleep(0.1)
