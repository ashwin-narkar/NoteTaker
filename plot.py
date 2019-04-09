#!/usr/bin/python
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from scipy.io import wavfile


def getHzofChunk(chunk,binsize):
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	return (argmax(mag)*binsize/2)

def plotChunk(chunk):
	plt.figure(1)
	plt.plot(amplitude[0:chunksize])
	plt.figure(2)
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	plt.plot(fftMag)
	plt.show()


def main():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	amplitude = data[:,0]
	chunksize = 2205
	binsize = fs/chunksize
	
	note = getHzofChunk(amplitude[0:chunksize])



if __name__ == "__main__":
	main()
