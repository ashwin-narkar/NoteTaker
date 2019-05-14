#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment
from normalize import*
from scipy.signal import firwin, lfilter
from scipy.io import wavfile

def lowpass(sr, data):
    b = firwin(101, cutoff = 600, nyq = sr/2, pass_zero = True)
    data = lfilter(b, [1.0], data)
    wavfile.write('./musicFiles/testLow.wav', sr, normalized_sound.astype(np.int16))
    normalized_sound = normalize("./musicFiles/testLow.wav", -10.0)

def highpass(sr, data):
    b = firwin(101, cutoff = 1000, nyq = sr/2, pass_zero = False)
    data = lfilter(b, [1.0], data)
    wavfile.write('./musicFiles/testHigh.wav', sr, normalized_sound.astype(np.int16))
    normalized_sound = normalize("./musicFiles/testHigh.wav", -10.0)

def main():
    filename = sys.argv[1]
    sr, data = wavfile.read(filename)
    #lowpass(sr, data)
    #highpass(sr, data)

if __name__ == "__main__":
	main()
