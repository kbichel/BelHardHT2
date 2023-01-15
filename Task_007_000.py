###The program throws errors if: 1.A letter is entered instead of number;2.There is a division by zero;3.There are no real roots.
###

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    a = float(input('Please enter a: '))
    b = float(input('Please enter b: '))
    c = float(input('Please enter c: '))
    d = b*b - 4*a*c

    if a==0:
        raise ZeroDivisionError("Please try a different value of 'a', non-zero.")
    else:
        if d<0:
            raise Exception("There are no real roots as determinant is less than zero. Please try different values of a, b and c.")

except (ValueError):
    print('Please enter numerical values - real numbers.')
    #if a==0:
    #    print("Please try a different value of 'a', non-zero.")
    #if d<0:
    #   print("There are no real roots as determinant is less than zero. Please try different values of a, b and c.")
    exit()

else:
    print('Nothing went wrong. Please view the graphic solution.')

d = b*b - 4*a*c
x1=(-b + np.sqrt(d))/(2*a)
x2=(-b - np.sqrt(d))/(2*a)

if d>0:
    print(f'There are two distinct roots: {x1} and {x2}')
    xpoints=np.array([x1, x2])
    ypoints=np.array([0, 0])

if d==0:
    print(f'There are two repeated roots: x1 = x2 = {x1}')
    xpoints=np.array([0, x1])
    ypoints=np.array([0, 0])


#x = np.linspace(-5,5,100)
x = np.arange(-2, 2, 0.05)
y = a*(x**2) + b*x + c 
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(xpoints, ypoints, color='r', label='roots', marker='*')
plt.plot(x, y, color='b', label='function')
plt.show()