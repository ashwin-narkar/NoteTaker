#!/usr/bin/python3
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from chords import*
from scipy.io import wavfile
from duration import*
import subprocess


def getHzofChunk(chunk,binsize):
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	fftMag[0] = 0
	maxHz = (argmax(fftMag)*binsize/2)
	return chordDetect(fftMag,maxHz,binsize)

def analyzeNotes(chunk,peaks,FFTsize,fs):
	i = 0
	x = 1

	output = []
	i = peaks[0]
	freq = getHzofChunk(chunk[i:i+FFTsize],fs/FFTsize)
	output.append(freq)
	measuresLeft = 2

	while (x<len(peaks)):
		duration = peaks[x] - peaks[x-1]
		print(duration)
		print(duration/fs)
		if (duration/fs < durations[0]/2.0):
			x+=1
			continue
		duration = identifyDuration(duration/fs)

		if (duration != "4."):
			measuresLeft -= (1/int(duration))
		else:
			measuresLeft -= 0.375
		output.append(duration)
		i = peaks[x]
		freq = getHzofChunk(chunk[i:i+FFTsize],fs/FFTsize)
		output.append(freq)
		x+=1

	duration = int(1/measuresLeft)
	print(measuresLeft)
	output.append(str(duration))
	# print(output)
	return(output)


def main():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	# print(len(notes))
	# print(len(frequencies))

	BPM = 150
	durationsInit(BPM)
	print(durations)
	amplitude = []
	chunkSize = 60.0/BPM #quarter note duration
	chunkSize *= 8 #4 notes per measure
	chunkSize *= fs

	chunkSize = int(chunkSize)
	# print(chunkSize)
	fftSize = 2205
	MAS = 200
	hammingArr = np.hamming(2*MAS)
	for i,j in data:
		x = (int(i))
		amplitude.append(x)
	startFile()
	q = 0

	peak = []

	print("Analyzing Recording: " + str((q/len(amplitude))*100) + "%")
	while (q < len(amplitude)-chunkSize):
		chunkArr = amplitude[q:q+chunkSize]
		# plt.plot(chunkArr)
		# plt.show()
		peak = logDeriv(chunkArr,MAS,hammingArr)
		notesArr = analyzeNotes(chunkArr,peak,fftSize,fs)
		writeToFile(notesArr)
		q+=chunkSize
		print("Analyzing Recording: " + str(int((q/len(amplitude))*100.0)) + "%")
	chunkArr = amplitude[q:]
	peak = logDeriv(chunkArr,MAS,hammingArr)

	notesArr = analyzeNotes(chunkArr,peak,fftSize,fs)
	writeToFile(notesArr)
	# print(peak)
	# notesArr = analyzeRecording(chunkToAnalyze,chunksize,binsize)
	# writeToFile(notesArr)
	endFile()
	print("Analysis Complete!")



if __name__ == "__main__":
	main()
