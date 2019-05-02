#!/usr/bin/python3
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from scipy.io import wavfile

def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))

def analyzeChunk(chunk,mPofChunk):
	i=0
	firstNote = True
	noteBeginning = 0
	noteEnd = 0
	noteActive = False
	duration = 0
	
	while (firstNote):
		if (mPofChunk[i] > mPofChunk[i-1]):
			noteBeginning = i
			firstNote=False
			noteActive = True
		i+=1
	while (i< len(mPofChunk)):
		
		if (mPofChunk[i] - mPofChunk[i-2] > 1500 and noteActive):
			noteEnd = i
			duration = noteEnd - noteBeginning
			if (duration<=3):
				i+=1
				continue
			print("Note lasted " + str(duration))
			noteBeginning = i+1
			#do FFT and quantize duration to BPM
		elif (mPofChunk[i] < 550 and noteActive):
			noteEnd = i
			duration = noteEnd - noteBeginning
			print("Note lasted " + str(duration))
			# do FFT and quantize duration to BPM
			noteActive = False
		elif (mPofChunk[i] > 2500 and noteActive == False):
			noteBeginning = i
			noteActive = True
		i+=1


def temp():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	amplitudeL = []
	amplitudeR = []
	for i,j in data:
		amplitudeL.append(j)
		amplitudeR.append(i)
	plt.figure()
	plt.plot(amplitudeL)
	averagePlot = []
	y = 0
	every100Plot = []
	i = 0
	BPM = 150
	MAS=500
	while (i < len(amplitudeL)-MAS):
		every100Plot.append(max(absolute(amplitudeL[i:i+MAS])))
		moving_average = 0
		for x in range(MAS):
			moving_average = moving_average+ (absolute(amplitudeL[x+i])/MAS)
		#moving_average/=MAS
		averagePlot.append(moving_average)
		i+=MAS
	i = 0
	chunkSize = 60/BPM #quarter note duration
	chunkSize *= 4 #4 notes per measure
	chunkSize *= fs
	chunkSize = int(chunkSize)

	while (i<len(amplitudeL)-chunkSize):
		currAvg = averagePlot[int(i/MAS) : int((i+chunkSize)/MAS)]
		
		for x in range(15):
			currAvg.insert(0,currAvg[0])
		
		plt.figure()
		plt.plot(result["signals"])
		print("")
		i+=chunkSize

	currAvg = averagePlot[int(i/MAS):]
	for x in range(15):
		currAvg.insert(0,currAvg[0])
	
	plt.figure()
	plt.plot(currAvg)
	plt.figure()
	plt.plot(result["signals"])
	print("")
	i+=chunkSize

	
	plt.show()




def main():
	filename = sys.argv[1]
	fs, data = wavfile.read(filename)
	energy = []
	averagePlot = []
	MAS = 200
	for i,j in data:
		x = (int(i))*(int(i))
		energy.append(x)
	i = 0
	while (i < len(energy)-MAS):
		
		moving_average = 0
		for x in range(MAS):
			moving_average += (-moving_average/MAS)+ (absolute(energy[x+i])/MAS)
		averagePlot.append(moving_average)
		i+=MAS
	plt.figure()
	plt.plot(energy)
	plt.figure()
	plt.plot(log(averagePlot))
	plt.show()


if __name__ == "__main__":
	main()
