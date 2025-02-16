if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
from mydezero import Function, Variable

class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y
    
    def backward(self, gy):
        x = self.inputs[0].data
        gx = gy * np.cos(x)
        return gx

def sin(x):
    return Sin()(x)

import math 
def my_sin(x, threshold=0.0001):
    y = 0
    for i in range(100000):
        c = (-1)**i/math.factorial(2*i+1)
        t = c * x**(2*i+1)
        y = y+t
        if abs(t.data) < threshold:
            break
    return y


def rosenbrock(x0, x1):
    y = 100*(x1-x0**2)**2 + (1-x0)**2
    return y

def f(x):
    y = x**4-2*x**2
    return y

from mydezero import Function, Variable
import mydezero.functions as F
import matplotlib.pyplot as plt

x = Variable(np.linspace(-7, 7, 200))
y = F.sin(x)
y.backward(create_graph=True)
logs = [y.data]

for i in range(3):
    logs.append(x.grad.data)
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)
    print(x.grad)
    
labels = ['y=sin(x)', "y'", "y''", "y'''"]
for i, v in enumerate(logs):
    plt.plot(x.data, logs[i], label=labels[i])
plt.legend(loc = 'lower right')
plt.show()