#!/usr/bin/python3
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from scipy.io import wavfile
from duration import*
import subprocess


def getHzofChunk(chunk,binsize):
	fftOut = fft.rfft(chunk)
	fftMag = absolute(fftOut)
	return (argmax(fftMag)*binsize/2)

def plotChunk(chunk):
	# plt.figure(1)
	plt.plot(absolute(chunk))
	# plt.figure(2)
	# fftOut = fft.rfft(chunk)
	# fftMag = absolute(fftOut)
	# plt.plot(fftMag)
	
def analyzeNotes(chunk,peaks,FFTsize,fs):
	i = 0
	x = 1
	output = []
	i = peaks[0]
	freq = getHzofChunk(chunk[i:i+FFTsize],fs/FFTsize)
	output.append(identifyNote(freq))
	measuresLeft = 2

	while (x<len(peaks)):
		duration = peaks[x] - peaks[x-1]
		duration = identifyDuration(duration/22050.0)
		if (duration != "4."):
			measuresLeft -= (1/int(duration))
		else:
			measuresLeft -= 0.375
		output.append(duration)
		i = peaks[x]
		freq = getHzofChunk(chunk[i:i+FFTsize],fs/FFTsize)
		output.append(identifyNote(freq))
		x+=1
	
	duration = int(1/measuresLeft)
	output.append(str(duration))
	# print(output)
	return(output)

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

	
	BPM = 150
	durationsInit(BPM)
	amplitude = []
	chunkSize = 60/BPM #quarter note duration
	chunkSize *= 8 #4 notes per measure
	chunkSize *= fs
	chunkSize = int(chunkSize)
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
		peak = logDeriv(chunkArr,MAS,hammingArr)
		notesArr = analyzeNotes(chunkArr,peak,fftSize,fs)
		writeToFile(notesArr)
		q+=chunkSize
		print("Analyzing Recording: " + str(int((q/len(amplitude))*100)) + "%")
	chunkArr = amplitude[q:]
	peak = logDeriv(chunkArr,MAS,hammingArr)
	notesArr = analyzeNotes(chunkArr,peak,fftSize,fs)
	writeToFile(notesArr)
	# print(peak)
	# notesArr = analyzeRecording(chunkToAnalyze,chunksize,binsize)
	# writeToFile(notesArr)
	endFile()
	print("Analysis Complete!")
	print()
	subprocess.run(["lilypond", "sheet.ly"])



if __name__ == "__main__":
	main()
