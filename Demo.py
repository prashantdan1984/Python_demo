# * patterns printiong
import numpy as np
import matplotlib as matplot
import pandas as pd

"""
P1
*
**
***
****
*****
"""
number =int(input("please enter the number for printing *"))
# with while loops
print("while loops P1")
i = 0
while i <= number:
    print(i * "* ")
    i += 1

# with for loops.
print("for loops P1")
for row in range(number+1):
    for col in range(row):
        print("*", end=' ')
    print()

"""
P2
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# with While loops
print("while loops P2")
i = 0
while i <= number-1:
    print(number * "* ")
    i += 1

# with for loops.
print("for loops P2")
for row in range(number):
    for col in range(number):
        print("*", end=' ')
    print()

"""
P3
* * * * *
* * * *
* * * 
* * 
* 
"""
# with While loops
print("while loops P3")
i = 0
while i <= number-1:
    print((number-i) * "* ")
    i += 1

# with for loops.
print("for loops P3")
for row in range(number):
    for col in range(number - row):
        print("*", end=' ')
    print()

"""
P4
      *
    * *
  * * * 
* * * * 
"""
# with While loops
print("while loops P4")
i = 0
while i <= number:
    print((number-i) * "  " + i * "* ")
    i += 1

# with for loops.
print("for loops P4")
for row in range(number+1):
    print((number-row) * "  " + row * "* ")
    

"""
P5
  *
 * *
* * *
"""
# with While loops
print("while loops P5")
i = 0
while i <= number:
    print((number-i) * " " + i * "* ")
    #print(i * "* ")
    i += 1

# with for loops.
print("for loops P5")
for row in range(number+1):
    print((number-row) * " " + row * "* ")
