# import numpy as np
# import weakref
# import contextlib

# class Config:
#     enable_backprop = True
        
# @contextlib.contextmanager
# def using_config(name, value):
#     old_value = getattr(Config, name)
#     setattr(Config, name, value)
#     try:
#         yield
#     finally:
#         setattr(Config, name, old_value)

# def no_grad():
#     return using_config('enable_backprop', False)

# class Variable:
#     ___array_priority__ = 200
#     def __init__(self, data, name=None):
#         if data is not None:
#             if not isinstance(data, np.ndarray):
#                 raise TypeError(f'{type(data)}는 지원하지 않습니다.')
            
#         self.data = data
#         self.name = name
#         self.grad = None
#         self.creator = None
#         self.generation = 0
        
#     def set_creator(self, func):
#         self.creator = func
#         self.generation = func.generation + 1
        
#     def cleargrad(self):
#         self.grad = None
    
#     def backward(self, retain_grad=False):
#         if self.grad is None: self.grad = np.ones_like(self.data)
#         funcs = []
#         seen_set = set()
        
#         def add_func(f):
#             if f not in seen_set:
#                 funcs.append(f)
#                 seen_set.add(f)
#                 funcs.sort(key=lambda x:x.generation)
        
#         add_func(self.creator)
        
#         while funcs:
#             f = funcs.pop()
#             gys = [output().grad for output in f.outputs]
#             gxs = f.backward(*gys)
#             if not isinstance(gxs, tuple):
#                 gxs = (gxs,)
#             for x, gx in zip(f.inputs, gxs):
#                 if x.grad is None:
#                     x.grad = gx
#                 else:
#                     x.grad = x.grad + gx
#                 if x.creator is not None:
#                     add_func(x.creator)
#             if not retain_grad:
#                 for y in f.outputs:
#                     y().grad = None
    
#     @property
#     def ndim(self):
#         return self.data.ndim
    
#     @property
#     def size(self):
#         return self.data.size
    
#     @property
#     def dtype(self):
#         return self.data.dtype
    
#     def __len__(self):
#         return len(self.data)
    
#     def __repr__(self):
#         if self.data is None:
#             return 'variable(none)'
#         p = str(self.data).replace('\n', '\n'+' '*9)
#         return f'variable({p})'


    
    
# class Function:
#     def __call__(self, *inputs):
#         inputs = [as_variable(x) for x in inputs]
        
#         xs = [x.data for x in inputs]
#         ys = self.forward(*xs)
#         if not isinstance(ys, tuple):
#             ys = (ys,)
#         outputs = [Variable(as_array(y)) for y in ys]
        
#         if Config.enable_backprop:
#             self.generation = max([x.generation for x in inputs])
#             for output in outputs:
#                 output.set_creator(self)
#             self.inputs = inputs
#             self.outputs = [weakref.ref(output) for output in outputs]
            
#         return outputs if len(outputs) > 1 else outputs[0]

#     def forward(self, x):
#         raise NotImplementedError()
    
#     def backward(self, gy):
#         raise NotImplementedError()
    
    
    
    
# class Square(Function):
#     def forward(self, x):
#         return x**2
    
#     def backward(self, gy):
#         x = self.inputs[0].data
#         gx = 2*x*gy
#         return gx
    
    
# class Exp(Function):
#     def forward(self, x):
#         return np.exp(x)
    
#     def backward(self, gy):
#         x = self.inputs[0].data
#         gx = np.exp(x)*gy
#         return gx

# class Add(Function):
#     def forward(self, x0, x1):
#         y = x0 + x1
#         return y
    
#     def backward(self, gy):
#         return gy, gy

# class Mul(Function):
#     def forward(self, x0, x1):
#         y = x0 * x1
#         return y
    
#     def backward(self, gy):
#         x0, x1 = self.inputs[0].data, self.inputs[1].data
#         return gy*x1, gy*x0

# class Neg(Function):
#     def forward(self, x):
#         return -x
    
#     def backward(self, gy):
#         return -gy
    
# class Sub(Function):
#     def forward(self, x0, x1):
#         y = x0 - x1
#         return y
    
#     def backward(self, gy):
#         return gy, -gy

# class Div(Function):
#     def forward(self, x0, x1):
#         y = x0/x1
#         return y
    
#     def backward(self, gy):
#         x0, x1 = self.inputs[0].data, self.inputs[1].data
#         gx0 = gy/x1
#         gx1 = gy*(-x0/x1**2)
#         return gx0, gx1
    
# class Pow(Function):
#     def __init__(self, c):
#         self.c = c
        
#     def forward(self, x):
#         y = x**self.c
#         return y
    
#     def backward(self, gy):
#         x = self.inputs[0].data
#         c = self.c
#         gx = c*x**(c-1)*gy
#         return gx

# def numerical_diff(f, x, eps=1e-4):
#     x0 = Variable(x.data - eps)
#     x1 = Variable(x.data + eps)
#     y0 = f(x0)
#     y1 = f(x1)
#     return (y1.data - y0.data) / (2 * eps)

# def as_variable(obj):
#     if isinstance(obj, Variable):
#         return obj
#     return Variable(obj)

# def as_array(x):
#     if np.isscalar(x):
#         return np.array(x)
#     return x

# def square(x):
#     f = Square()
#     return f(x)

# def exp(x):
#     f = Exp()
#     return f(x)

# def add(x0, x1):
#     x1 = as_array(x1)
#     return Add()(x0, x1)

# def mul(x0, x1):
#     x1 = as_array(x1)
#     return Mul()(x0, x1)

# def neg(x):
#     return Neg()(x)

# def sub(x0, x1):
#     x1 = as_array(x1)
#     return Sub()(x0, x1)

# def rsub(x0, x1):
#     x1 = as_array(x1)
#     return Sub()(x1, x0)

# def div(x0, x1):
#     x1 = as_array(x1)
#     return Div()(x0, x1)

# def rdiv(x0, x1):
#     x1 = as_array(x1)
#     return Div()(x1, x0)

# def pow(x, c):
#     return Pow(c)(x)



# import unittest

# class SquareTest(unittest.TestCase):
#     def test_forward(self):
#         x = Variable(np.array(2.0))
#         y = square(x)
#         expected = np.array(4.0)
#         self.assertEqual(y.data, expected)
    
#     def test_backward(self):
#         x = Variable(np.array(3.0))
#         y = square(x)
#         y.backward()
#         expected = np.array(6.0)
#         self.assertEqual(x.grad, expected)
        
#     def test_gradient_check(self):
#         x = Variable(np.random.rand(1))
#         y = square(x)
#         y.backward()
#         num_grad = numerical_diff(square, x)
#         flg = np.allclose(x.grad, num_grad)
#         self.assertTrue(flg)





# Variable.__add__ = add
# Variable.__radd__ = add
# Variable.__mul__ = mul
# Variable.__rmul__ = mul
# Variable.__neg__ = neg
# Variable.__sub__ = sub
# Variable.__rsub__ = rsub
# Variable.__truediv__ = div
# Variable.__rtruediv__ = rdiv
# Variable.__pow__ = pow
if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from mydezero import Variable

def sphere(x, y):
    z = x ** 2 + y ** 2
    return z


def matyas(x, y):
    z = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    return z


def goldstein(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * \
        (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return z


x = Variable(np.array(1.0))
y = Variable(np.array(1.0))
z = goldstein(x, y)  
z.backward()
print(x.grad, y.grad)