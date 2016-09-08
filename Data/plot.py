# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
from scipy import interpolate 

seed = '1212'
t = [(x+1)*50 for x in xrange(240)]

def value(seed,mode,file,loc):
	data = np.loadtxt(seed+ '/' + file +'_m'+ mode +'.csv',dtype='string',delimiter=',')

	v = []
	
	for i in xrange((len(data)-1)/50):
		line = data[(i+1)*50]
		v.append(float(line[loc]))
	tck = interpolate.splrep(t,v)
	# tck_2 = interpolate.splrep(t)
	v_bspline = interpolate.splev(t,tck)
	return v_bspline

def Quality(seed,mode,style):
	data = np.loadtxt(seed+ '/Quality_m'+ mode +'.csv',dtype='string',delimiter=',')
	tick = []
	q = []
	
	for i in xrange((len(data)-1)/50):
		line = data[(i+1)*50]
		tick.append(float(line[0]))
		q.append(float(line[1]))
	f2 = interpolate.interp1d(tick, q, kind='cubic')
	plt.plot(tick,f2(tick),style,markevery=8)

def myplot(x,style):
	plt.plot(t,x,style,markevery=8)


styles = ['b-o','g:o','r-s','c:s','k-^','m:^']
modes = ['11','12','21','22','31','32']
plt.figure(figsize=(16,15))
# tck = interpolate.splrep(t,N_T)
# tck_2 = interpolate.splrep(t)
# x_bspline = interpolate.splev(t,tck)
# markers_on = [12, 17, 18, 19]
# plt.plot(xs, ys, '-gD', markevery=markers_on)

plt.subplot(421)
for i in range(6):
	style = styles[i]
	N_R = value(seed,modes[i],'Machine',1)
	myplot(N_R,style)

plt.title(r'Number of resources($N_R$)')

plt.subplot(422)
for i in range(6):
	style = styles[i]
	N_P = value(seed,modes[i],'Provider',1)
	myplot(N_P,style)
plt.title(r'Number of providers($N_P$)')

plt.subplot(423)
for i in range(6):
	style = styles[i]
	N_T = value(seed,modes[i],'Task',1)
	myplot(N_T,style)
plt.title(r'Number of tasks($N_T$)')

plt.subplot(424)
for i in range(6):
	style = styles[i]
	N_F = value(seed,modes[i],'Finish',1)
	myplot(N_F,style)
plt.title(r'Accumulation of finished tasks($N_F$)')

plt.subplot(425)
for i in range(6):
	style = styles[i]
	N_R = value(seed,modes[i],'Qualities',1)
	myplot(N_R,style)
plt.title(r'Maximum queue length($L$)')

plt.subplot(426)
for i in range(6):
	style = styles[i]
	R = value(seed,modes[i],'Qualities',4)
	myplot(R,style)
plt.title(r'Maximum rank value($R$)')
plt.xlabel("Time tick")
plt.subplot(427)
# f = Quality(seed,modes[0])

for i in range(6):
	style = styles[i]
	Quality(seed,modes[i],style)
# 	myplot(f(t),style)
plt.title(r'Product quality($Q$)')
plt.xlabel("Time tick")
plt.subplot(428)
plt.axis('off')
for style in styles:
	plt.plot(1,1,style)

plt.legend(['Mode 11','Mode 12','Mode 21','Mode 22','Mode 31','Mode 32'],loc='center')

plt.savefig('out_new.pdf', transparent=True, bbox_inches='tight', pad_inches=0)
plt.savefig('out_new.eps', transparent=True, bbox_inches='tight', pad_inches=0)


def mymean(seed,mode,file,loc):
	data = np.loadtxt(seed+ '/' + file +'_m'+ mode +'.csv',dtype='string',delimiter=',')

	v = []
	
	for i in xrange((len(data)-1)):
		line = data[(i+1)]
		v.append(float(line[loc]))
	
	return round(np.mean(v),3)

	# l = [mymean(seed,mode,'Task',0),mymean(seed,mode,'FinishCount',1),mymean(seed,mode,'Provider'，1)]#,mymean(seed,mode,'Machine',1),mymean(seed,mode,'Quality',1)]
# mymean(seed,'11','Provider',1)
# for mode in modes:
# 	# print "Mode " +mode + '\n'
# 	l = [mymean(seed,mode,'Task',1),mymean(seed,mode,'Finish',1),mymean(seed,mode,'Provider',1),mymean(seed,mode,'Machine',1),mymean(seed,mode,'Quality',1)]
# 	print l
	# print '\n'
