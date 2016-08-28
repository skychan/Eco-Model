# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
from scipy import interpolate 

data = np.loadtxt('test',dtype='string',delimiter=',')
x = []
y = []
t = []
for i in xrange((len(data)-1)/50):
	line = data[(i+1)*50]
	x.append(float(line[0]))
	y.append(float(line[2]))
	t.append(float(line[1]))



plt.figure(figsize=(15,15))
tck = interpolate.splrep(t,x)
# tck_2 = interpolate.splrep(t)
x_bspline = interpolate.splev(t,tck)
# markers_on = [12, 17, 18, 19]
# plt.plot(xs, ys, '-gD', markevery=markers_on)

plt.subplot(421)
plt.plot()
plt.title(r'Number of resources($N_R$)')

plt.subplot(422)
plt.plot()
plt.title(r'Number of providers($N_P$)')

plt.subplot(423)
plt.plot()
plt.title(r'Number of tasks($N_T$)')

plt.subplot(424)
plt.plot()
plt.title(r'Accumulation of finished tasks($N_F$)')

plt.subplot(425)
plt.plot(t,x_bspline,marker='o',markevery=8)
plt.title(r'Maximum queue length($L$)')

plt.subplot(426)
plt.plot()
plt.title(r'Maximum rank value($R$)')

plt.subplot(427)
plt.plot(t,x_bspline,marker='o',markevery=8)
plt.title(r'Product quality($Q$)')

plt.subplot(428)
plt.axis('off')
plt.plot(1,1,'-',marker='o')
plt.plot(1,1,':',marker='o')
plt.plot(1,1,'-',marker='s')
plt.plot(1,1,':',marker='s')
plt.plot(1,1,'-',marker='v')
plt.plot(1,1,':',marker='v')
plt.legend(['Mode 11','Mode 12','Mode 21','Mode 22','Mode 31','Mode 32'],loc='center')

plt.savefig('out.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


