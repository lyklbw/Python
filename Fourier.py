import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft,rfftfreq
from scipy.fft import irfft
plt.rcParams['figure.figsize'] = [16,10]
plt.rcParams.update({'font.size':18})

#Create a simple signal with two frequencies
data_step   = 0.001
t           = np.arange(start=0,stop=1,step=data_step)
f_clean     = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f_noise     = f_clean + 2.5*np.random.randn(len(t))


n    = len(t)
yf   = rfft(f_noise)
xf   = rfftfreq(n,data_step)
yf_abs      = np.abs(yf) 
indices     = yf_abs>300   # filter out those value under 300
yf_clean    = indices * yf # noise frequency will be set to 0
new_f_clean = irfft(yf_clean)
plt.plot(t,new_f_clean,color='blue',label='Filtered')
plt.plot(t,f_clean,color='black',label='Clean')
plt.ylim(-6,8)
plt.show()