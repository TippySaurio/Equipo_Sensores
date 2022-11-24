# ky-009

## Code
```python
#Diaz Rodriguez Jorge Said 19211629
# MicroPhyton
from machine import Pin, ADC
from time import sleep
a0 = ADC(Pin(27))
while True:
    value = a0.read_u16()
   
    
    print("value: " + str(value))
    print(" ")
    
```
## Result
![](https://media0.giphy.com/media/go8UAXKx6GHRJVtUBL/giphy.gif?cid=790b7611e2bd9ea5226e2a9d00d1896d736dedb60477cfd2&rid=giphy.gif&ct=g)
