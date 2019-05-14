#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment
from scipy.signal import firwin, lfilter
from scipy.io import wavfile

def lowpass(sr, data):
    b = firwin(101, cutoff = 600, nyq = sr/2, pass_zero = True)
    data = lfilter(b, [1.0], data)
    wavfile.write('testlow.wav', sr, data.astype(np.int16))

def highpass(sr, data):
    b = firwin(101, cutoff = 1000, nyq = sr/2, pass_zero = False)
    data = lfilter(b, [1.0], data)
    wavfile.write('testhigh.wav', sr, data.astype(np.int16))

def main():
    filename = sys.argv[1]
    sr, data = wavfile.read(filename)
    song = AudioSegment.from_wav(filename)

    # reduce volume by 10 dB
    song_10_db_quieter = song - 1

    #lowpass(sr, data)
    #highpass(sr, data)

if __name__ == "__main__":
	main()
