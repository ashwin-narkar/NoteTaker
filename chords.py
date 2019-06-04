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

    ff = 0.08;
    thresh = np.std(fftMag) * 6 + np.average(fftMag)
    # plt.plot(fftMag)
    # plt.hlines(thresh, 0, len(fftMag))
    # plt.show()
    #checkFreq = Hz
    foundHz = Hz           #set foundHz to freq at 1.5 times the checkFreq first

    rootConfirmed = False
    fifthConfirmed = False
    thirdConfirmed = False
    chordFound = False

    nord = ""
    #print(foundHz *2 / binsize)
    #print (fifthFreq)

#--------------------------------------\/ROOT FIRST\/-------------------------------------
    fifthFreq = math.floor(foundHz * 1.5 * 2 / binsize)

    for i in range(-1, 2):
        if fftMag[fifthFreq + i] > thresh and rootConfirmed==False:
            rootNote = identifyNote(foundHz)
            fifthNote = identifyNote(fifthFreq * binsize / 2)
            #print("Found the root note " + str(rootNote) + " and verified fifth")
            rootConfirmed = True
            nord = "<" + str(rootNote)

    majorThirdFreq = math.floor(foundHz * 1.25 * 2 / binsize)

    if rootConfirmed == True:
        for i in range(-1, 2):
            if fftMag[majorThirdFreq + i] > thresh and chordFound== False:
                thirdNoteHz = (majorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                #print("Found a major chord")                       #Found matching major third based on if peak Hz is root
                chordFound = True
                nord +=  " " + str(thirdNote) + " " + str(fifthNote) + ">"


    minorThirdFreq = math.floor(foundHz * 1.2 * 2 / binsize)
    if rootConfirmed == True:
        for i in range(-1, 2):
            if fftMag[minorThirdFreq + i] > thresh and chordFound==False:
                thirdNoteHz = (minorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                nord +=  " " + str(thirdNote) + " " + str(fifthNote) + ">"
                #print("Found a minor chord")                       #Found matching minor third based on if peak Hz is root
    if chordFound:
        print (nord)
        return nord

    #plt.show()
#--------------------------------------^ROOT FIRST^---------------------------------------



#--------------------------------------\/FIFTH FIRST\/-------------------------------------
    rootNoteFreq = math.floor(foundHz / 1.5 * 2 / binsize)

    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh and fifthConfirmed==False:
            fifthNote = identifyNote(foundHz)
            rootNote = identifyNote(rootNoteFreq*binsize/2)
            #print("Peak at fifth and root found at " + str(rootNote))
            nord = "<" + str(rootNote)
            fifthConfirmed = True

    majorThirdFreq = math.floor(rootNoteFreq * 1.25)

    for i in range(-1, 2):
        if fifthConfirmed == True:
            if fftMag[majorThirdFreq + i] > thresh and chordFound==False:
                thirdNoteHz = (majorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                nord += " " + str(thirdNote) + " " + str(fifthNote) + ">"
                #print("Found major chord")

    minorThirdFreq = math.floor(rootNoteFreq * 1.2)

    for i in range(-1, 2):
        if fifthConfirmed == True:
            if fftMag[minorThirdFreq + i] > thresh and chordFound==False:
                thirdNoteHz = (minorThirdFreq + i) * binsize / 2
                thirdNote = identifyNote(thirdNoteHz)
                chordFound = True
                nord += " " + str(thirdNote) + " " + str(fifthNote) + ">"
                #print("Found minor chord")

    if chordFound:
        print (nord)
        return nord
#--------------------------------------^FIFTH FIRST^---------------------------------------



#--------------------------------------\/THIRD FIRST\/-------------------------------------
    rootNoteFreq = math.floor(foundHz * 0.8 * 2 / binsize)
    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh and thirdConfirmed == False:
            thirdNote = identifyNote(foundHz)
            rootNote = identifyNote(rootNoteFreq*binsize/2)
            thirdConfirmed = True
            nord = "<" + str(rootNote) + " " str(thirdNote) + " "
            #print("Peak at major third with root at " + str(rootNote))


    rootNoteFreq = math.floor(foundHz / 6 * 5)

    for i in range(-1, 2):
        if fftMag[rootNoteFreq + i] > thresh and thirdConfirmed == False:
            rootNote = identifyNote(rootNoteFreq * binsize/2)
            thirdConfirmed = True
            nord = "<" + str(rootNote) + " " str(thirdNote) + " "
            #print("Peak at minor third with root at " + str(rootNote))

    if (thirdConfirmed):
        fifthFreq = math.floor(rootNoteFreq * 1.5)
        for i in range(-1, 2):
            if fftMag[fifthFreq + i] > thresh and chordFound==False:
                fifthNote = identifyNote(fifthFrew * binsize / 2)
                #print("Found the fifth")
                nord += str(fifthNote) + ">"
                chordFound = True

    if chordFound:
        print (nord)
        return nord
#--------------------------------------^THIRD FIRST^---------------------------------------

    if chordFound == False:
        print(identifyNote(Hz))
        nord = identifyNote(Hz)
        return str(nord)
    #plt.show()
