import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Solve a quadratic equation
#a = float(input('Please enter a: '))
#b = float(input('Please enter a: '))
#c = float(input('Please enter a: '))
#a*x^2 + b*x + c =0
a = float(input('Please enter a: '))
b = float(input('Please enter a: '))
c = float(input('Please enter a: '))

#x = np.linspace(-5,5,100)
x = np.arange(-2, 2, 0.05)
y = a*(x**2) + b*x + c 
d = b*b - 4*a*c

if d<0:
    raise Exception('There are no real roots as determinant is less than zero')
#elif a<0:
    #raise Exception('Division by 0 is not allowed - try value of a which is not zero')

try:
    #print('determinant is \n',d)
    #if d==0:
        #print("The determinant is zero, so there are two repeated roots.")
    x1=(-b + np.sqrt(d))/(2*a)
    x2=(-b - np.sqrt(d))/(2*a)
    #print(x1,x2)
    if d>0:
        print(f'There are two distinct roots: {x1} and {x2}')
        xpoints=np.array([x1, x2])
        ypoints=np.array([0, 0])


    if d==0:
        print(f'There are two repeated roots: x1 = x2 = {x1}')
        xpoints=np.array([0, x1])
        ypoints=np.array([0, 0])


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

except:
    print("Try different values a, b and c")