from scipy import optimize
import scipy.io as spio
import numpy as np
from scipy import stats  # same for other sub-modules
from scipy import misc
from scipy import linalg
from scipy import fftpack
from matplotlib import pyplot as plt
def f(x):
    return x**2 + 10*np.sin(x)
x = np.arange(-10, 10, 0.1)
print f(x)
st1=optimize.fmin_bfgs(f, 3, disp=0)
print st1, f(st1)
plt.plot(x, f(x)) 
plt.show()
st=optimize.fmin_bfgs(f, 0)
print st