# ky-038

## Code

```python
import machine
import utime
import math

pot_pin = machine.ADC(26) 

while True:
    pot_val = pot_pin.read_u16()
    print(pot_val)
    utime.sleep(1)
   
    

```

## Result

 ![](https://media2.giphy.com/media/D8mWRFuUpzvIdGSSmg/giphy.gif?cid=790b7611f17ad2d3d27a4a3f375f6fc253b06522f7fbc4a5&rid=giphy.gif&ct=g)
