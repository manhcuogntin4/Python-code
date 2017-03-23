import scipy.io as spio
import numpy as np
from scipy import stats  # same for other sub-modules
from scipy import misc
from scipy import linalg
from scipy import fftpack
from matplotlib import pyplot as plt
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + \
      0.5 * np.random.randn(time_vec.size)
plt.plot(time_vec,sig)
plt.show()

sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
plt.plot(time_vec, sig_fft)
plt.show()

pidxs = np.where(sample_freq > 0)
freqs = sample_freq[pidxs]
power = np.abs(sig_fft)[pidxs]

plt.plot(freqs,power)
plt.show()

arr = np.array([[1, 2],
                [3, 4]])
print linalg.det(arr)
iarr = linalg.inv(arr)
print iarr
st= misc.imread('../python.png')
#print st
a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a}) # savemat expects a dictionary
data = spio.loadmat('file.mat', struct_as_record=True)
print data['a']