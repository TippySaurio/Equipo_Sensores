# ky-023

## Code

```python
#Cruz Ruiz Luis Angel 19211621
from machine import Pin, ADC
from time import sleep

VRX = ADC(Pin(27))
VRY = ADC(Pin(26))
SW = Pin(22,Pin.IN, Pin.PULL_UP)

while True:
    xAxis = VRX.read_u16()
    yAxis = VRY.read_u16()
    switch = SW.value()
    
    print("X-axis: " + str(xAxis) + ", Y-axis: " + str(yAxis) + ", Switch " + str(switch))
    if switch == 0:
        print("Push button pressed!")
    print(" ")
    sleep(1)

```

## Result

 ![](https://media0.giphy.com/media/lTe816njgVWNzxE3MN/giphy.gif?cid=790b76114d108604addc8d90eb6ca25b5e56eea0a91c9495&rid=giphy.gif&ct=g)
