#!/usr/bin/python
import sys
import numpy as np
from numpy import*
from scipy.io import wavfile

filename = sys.argv[1]
fs, data = wavfile.read(filename)
amplitude = data[:,0]
print len(amplitude)
# for i in amplitude:
# 	print i
fftOut = fft.rfft(amplitude[0:22049])
fftMag = absolute(fftOut)
# for i in fftMag:
# 	print i
hz = (argmax(fftMag[1:]))/2
print(hz)
'''
for i in range(0,44100*3,256):
	fftOut = fft.rfft(amplitude[i:i+256])
	fftMag = absolute(fftOut)
	print argmax(fftMag)
'''
