#!/usr/bin/python3
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from scipy.io import wavfile


def getHzofChunk(chunk,binsize):
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	return (argmax(fftMag)*binsize/2)

def plotChunk(chunk):
	plt.figure(1)
	#plt.plot(absolute(chunk))
	# plt.figure(2)
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	plt.plot(fftMag)
	plt.show()



def main():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	durationsInit(150)
	amplitude = data[:,0]
	chunksize = 2205
	binsize = fs/chunksize
	i=0
	MAS=100
	moving_average = 0
	averagePlot = []
	y = 0
	while (i < len(amplitude)-chunksize):
		moving_average = 0
		for x in range(MAS):
			moving_average = moving_average+ absolute(amplitude[x+i])
		moving_average/=MAS
		averagePlot.append(moving_average)
		i+=100
	plotChunk(amplitude)




if __name__ == "__main__":
	main()
