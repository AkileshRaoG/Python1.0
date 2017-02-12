# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cube=125
epsilon=0.01
guess=1
increment=1
num_guess=0
while abs(guess**3-cube) >= epsilon and guess <= cube:
    guess+=increment
    num_guess+=1
print('num_guesses= ',num_guess)
if abs(guess**3-cube) >= epsilon:
    print('Failed on cube root of ',cube)
else:
    print(guess,' is the cube root of ',cube)
"""
x = 25
epsilon = 0.01
step = 0.1dssdg
guess = 0.0

while guess <= x:

    if abs -(guess**2x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
   
    
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    """