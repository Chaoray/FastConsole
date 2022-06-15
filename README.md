# FastConsole
Fast Console Output on high refresh rate.  
  
### General output performance:  
![image](https://user-images.githubusercontent.com/65358638/173827057-7da4bfe7-5b94-42c6-b102-60d55cd33ccb.png)

Code:
```py
from time import perf_counter
from FastConsole import Console
import os

fc1 = Console((120, 200))
fc1.attach()

elapsedTime1 = perf_counter()
fc1.write("Hello, World")
elapsedTime1 = perf_counter() - elapsedTime1

fc1.detach()

elapsedTime2 = perf_counter()
print("Hello, World")
elapsedTime2 = perf_counter() - elapsedTime2

print('FastConsole: ' + str(1 / elapsedTime1))
print('Python clear: ' + str(1 / elapsedTime2))
```

### Clearing screen performance:  
![image](https://user-images.githubusercontent.com/65358638/173827297-25e92d09-6a7c-4df3-ba13-af9cc1c57be9.png)

Code:  
```py
from time import perf_counter
from FastConsole import Console
import os

fc1 = Console((120, 200))
fc1.attach()

elapsedTime1 = perf_counter()
fc1.write("Hello, World")
fc1.clear()
elapsedTime1 = perf_counter() - elapsedTime1

fc1.detach()

elapsedTime2 = perf_counter()
print("Hello, World")
os.system('cls')
elapsedTime2 = perf_counter() - elapsedTime2

print('FastConsole: ' + str(1 / elapsedTime1))
print('Python clear: ' + str(1 / elapsedTime2))
```

### Usage:
```py
from FastConsole import Console

fc = Console((120, 200)) # create a console with 120x200 size
fc.attach()
fc.write('Hello, world', 0, 0)
sleep(5)
fc.detach()
```
