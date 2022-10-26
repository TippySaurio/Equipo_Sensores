from machine import Pin, ADC
from time import sleep

analog_value = machine.ADC(26)
 
while True:
    reading = analog_value.read_u16()     
    print("Campo magnetico: ",reading)
    sleep(1)
