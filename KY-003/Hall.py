# Karla Chavez
#17210542
# Micropython

from machine import Pin  
import time,utime
 
he=Pin(26,Pin.IN)  
led=Pin(11,Pin.OUT)  
while True:  
   try:  
     if he.value() == 0:  
       led.value(0)  
     elif he.value()==1:  
       led.value(1)  
   except KeyboardInterrupt:  
     break 
