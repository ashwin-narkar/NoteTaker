#!/usr/bin/python
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
	plt.plot(absolute(chunk))
	# plt.figure(2)
	# fftOut = fft.rfft(chunk)
	# fftMag = absolute(fftOut)
	# plt.plot(fftMag)
	plt.show()

def analyzeRecording(amplitude,chunksize,binsize):
	i=0
	MAS=100
	moving_average = 0
	edge = False
	firstNoteDone = False
	prevNoteIndex = 0
	duration = 0
	prevMovingAvg = 0
	output = []
	while (i < len(amplitude)-chunksize):
		moving_average = 0
		for x in range(MAS):
			moving_average = moving_average+ absolute(amplitude[x+i])
		moving_average/=MAS
		i+=100
		if (moving_average>1250 and edge==False):
			if (firstNoteDone):
				duration = i - prevNoteIndex
				prevNoteIndex = i
				#print("Note duration=" + str(duration))
				duration = identifyDuration(duration/22050.0)
				output.append(duration)
				#print("")
			else:
				prevNoteIndex = i
				firstNoteDone = True
			#print("Edge found at " + str(i) + " Average="+str(moving_average))
			i+=30
			freq = getHzofChunk(amplitude[i:i+chunksize],binsize)
			#print(identifyNote(freq))

			output.append(identifyNote(freq))

			edge=True
		if (moving_average<750 and edge==True):
			edge=False
	return output

def analyzeRecording2(amplitude,chunksize,binsize):
	i=0
	MAS=100
	moving_average = 0
	edge = False
	firstNoteDone = False
	prevNoteIndex = 0
	duration = 0
	prevMovingAvg = 0
	output = []
	while (i < len(amplitude)-chunksize):
		moving_average = 0
		for x in range(MAS):
			moving_average = moving_average+ absolute(amplitude[x+i])
		moving_average/=MAS
		i+=100
		if (firstNoteDone):
			difference = moving_average - prevMovingAvg
			if (difference > (0.4*moving_average)):
				# print("Edge detected at " + str(i-50))
				edge = True
			else:
				edge = False
		else:
			prevMovingAvg = moving_average
			firstNoteDone = True
			prevNoteIndex = -10000
			continue
		prevMovingAvg = moving_average

		if (edge == True):

			duration = i - prevNoteIndex
			if (duration <= 700):
				continue
			prevNoteIndex = i
			freq = getHzofChunk(amplitude[i:i+chunksize],binsize)
			duration = identifyDuration(duration/22050.0)
			output.append(duration)
			output.append(identifyNote(freq))
	return output[1:]



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

	print(analyzeRecording(amplitude,chunksize,binsize))
	# plt.figure(1)
	# plt.plot(absolute(amplitude))

	# plt.figure(2)
	# plt.plot(averagePlot)
	# plt.show()

	# for i in range(0,len(amplitude),chunksize):
	# 	note = getHzofChunk(amplitude[i:i+chunksize],binsize)
	# 	print(note)
	# plotChunk(amplitude)



if __name__ == "__main__":
	main()
