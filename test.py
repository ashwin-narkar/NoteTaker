#!/usr/bin/python

import numpy as np
from numpy import*
from scipy.io import wavfile


fs, data = wavfile.read('A3.wav')
amplitude = data[:,0]
# for i in amplitude:
# 	print i
fftOut = fft.rfft(amplitude[0:22049])
fftMag = absolute(fftOut)
#for i in fftMag:
	#print i
print(argmax(fftMag))
'''
for i in range(0,44100*3,256):
	fftOut = fft.rfft(amplitude[i:i+256])
	fftMag = absolute(fftOut)
	print argmax(fftMag)
'''
