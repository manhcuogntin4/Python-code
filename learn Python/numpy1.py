import numpy as np
import timeit
import datetime
import time
import matplotlib.pyplot as plt
# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

class Timer(object):
    """A simple timer."""
    def __init__(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.

    def tic(self):
        # using time.time instead of time.clock because time time.clock
        # does not normalize for multithreading
        self.start_time = time.time()

    def toc(self, average=True):
        self.diff = time.time() - self.start_time
        self.total_time = self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls
        if average:
            return self.average_time
        else:
            return self.diff


timer = Timer()
timer.tic()
L = range(1000)
[i**2 for i in L]
timer.toc()
print "Normal method:", timer.total_time
timer.tic()
a = np.arange(1000)
a**2
timer.toc()
print "Numpy method: ", timer.total_time
a = np.array([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]])
print a
print a.ndim
print a.shape


x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.plot(x, y, 'o')

image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()
#print image
