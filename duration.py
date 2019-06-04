#!/usr/bin/python3
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import*
from notes import*
from file import*
from scipy.io import wavfile

def logDeriv(dataL,MAS,hammingArray):		#uses derivative of log(energy) to calculate onsets
	energy = []
	averagePlot = []
	for i in range(MAS):
		dataL.insert(0,0)
		dataL.append(0)
	i = MAS
	while (i < len(dataL)-MAS):
		e = 0
		for j in range(-MAS,MAS):
			e += dataL[i+j]*dataL[i+j]*hammingArray[j+MAS]
		e *= 1/(2*MAS)
		energy.append(e)
		i+=1

	logEnergy = []
	for x in energy:
		logEnergy.append(log(x))
	dE = np.diff(logEnergy)
	i = 0
	MAS = 100
	while (i < len(energy)-MAS):

		moving_average = 0
		for x in range(MAS):
			moving_average += (-moving_average/MAS)+ (absolute(dE[x+i])/MAS)
		averagePlot.append(moving_average)
		i+=MAS
	s = np.std(averagePlot)
	a = np.average(averagePlot)
	i = 9
	peaks = []
	while (i<len(averagePlot)):
		for j in range(10):
			if (averagePlot[i-j] > (a+3*s)):
				peaks.append(i*100)
				break
		i+=10

	# plt.figure()
	# plt.hlines(a, 0, len(averagePlot))
	# plt.hlines(a+(3*s),0,len(averagePlot))
	# plt.plot(averagePlot)
	
	# plt.show()

	return peaks
