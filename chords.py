#!/usr/bin/python3
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from notes import*

def chordDetect(fftMag, Hz, binsize):

    # check fifth first
    # check fifth above
    # frequency we found *1.5
    plt.plot(fftMag)
    ff = 0.08;
    thresh = np.std(fftMag) * 8 + np.average(fftMag)
    #checkFreq = Hz
    foundHz = Hz           #set foundHz to freq at 1.5 times the checkFreq first
    rootConfirmed = False
    fifthConfirmed = False
    chordFound = False
    #print(foundHz *2 / binsize)
    #print (fifthFreq)

#--------------------------------------\/ROOT FIRST\/-------------------------------------
    fifthFreq = math.floor(foundHz * 1.5 * 2 / binsize)
    for i in range(-1, 2):
        if fftMag[fifthFreq + i] > thresh:
            rootNote = identifyNote(foundHz)
            print("Found the root note " + str(rootNote) + " and verified fifth")
            rootConfirmed = True

    majorThirdFreq = math.floor(foundHz * 1.25 * 2 / binsize)

    if rootConfirmed == True:
        for i in range(-1, 2):
            if fftMag[majorThirdFreq + i] > thresh:
                thirdNoteHz = (majorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                print("Found a major chord")                       #Found matching major third based on if peak Hz is root
                chordFound = True

    minorThirdFreq = math.floor(foundHz * 1.2 * 2 / binsize)
    if rootConfirmed == True:
        for i in range(-1, 2):
            if fftMag[minorThirdFreq + i] > thresh:
                thirdNoteHz = (minorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                print("Found a minor chord")                       #Found matching minor third based on if peak Hz is root


    #plt.show()
#--------------------------------------^ROOT FIRST^---------------------------------------



#--------------------------------------\/FIFTH FIRST\/-------------------------------------
    rootNoteFreq = math.floor(foundHz / 1.5 * 2 / binsize)
    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh:
            rootNote = identifyNote(rootNoteFreq)
            print("Peak at fifth and root found at " + str(rootNote))
            fifthConfirmed = True

    majorThirdFreq = math.floor(rootNoteFreq * 1.25 * 2 / binsize)

    for i in range(-1, 2):
        if fifthConfirmed == True:
            if fftMag[majorThirdFreq + i] > thresh:
                thirdNoteHz = (majorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                print("Found major chord")

    minorThirdFreq = math.floor(rootNoteFreq * 1.2 * 2 / binsize)

    for i in range(-1, 2):
        if fifthConfirmed == True:
            if fftMag[minorThirdFreq + i] > thresh:
                thirdNoteHz = (minorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                print("Found minor chord")
#--------------------------------------^FIFTH FIRST^---------------------------------------



#--------------------------------------\/THIRD FIRST\/-------------------------------------
    rootNoteFreq = math.floor(foundHz * 0.8 * 2 / binsize)
    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh:
            rootNote = identifyNote(rootNoteFreq)
            chordFound = True
            print("Peak at major third with root at " + str(rootNote))

    rootNoteFreq = math.floor(foundHz / 6 * 5 * 2 / binsize)

    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh:
            rootNote = identifyNote(rootNoteFreq * binsize/2)
            chordFound = True
            print("Peak at minor third with root at " + str(rootNote))


    fifthFreq = math.floor(rootNoteFreq * 1.5 * 2 / binsize)
    for i in range(-1, 2):
        if fftMag[fifthFreq + i] > thresh:
            rootNote = identifyNote(rootNoteFreq)
            print("Found the fifth")
#--------------------------------------^THIRD FIRST^---------------------------------------

    if chordFound == False:
        print("Single note: " + identifyNote(Hz))
    #plt.show()
