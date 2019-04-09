#!/usr/bin/python
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from scipy.io import wavfile


def getFFT(signal):
	fftOut = fft.rfft(signal)
	fftMag = absolute(fftOut)
	return fftMag

def main():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	amplitude = data[:,0]
	mag = getFFT(amplitude)
	plt.plot(mag)
	plt.show()	


if __name__ == "__main__":
	main()
