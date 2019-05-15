#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment
from normalize import*
from scipy.signal import firwin, lfilter
from scipy.io import wavfile

def lowpass(sr, data):
    b = firwin(5, cutoff = 400, nyq = sr/2, pass_zero = True)
    data = normalize("./musicFiles/furTest.wav", -20.0)
    data = lfilter(b, [1.0], data.get_array_of_samples())
    data = np.array(data)
    # data = data.low_pass_filter(400)
    # data.export("./musicFiles/testLow.wav", format = "wav")
    wavfile.write("./musicFiles/testLow.wav", sr, data.astype(np.int16))
    #data.export("./musicFiles/testLowNorm.wav", format = "wav")

def highpass(sr, data):
    # b = firwin(101, cutoff = 1000, nyq = sr/2, pass_zero = False)
    # data = lfilter(b, [1.0], data)
    data = data.high_pass_filter(1000)
    # wavfile.write("./musicFiles/testHigh.wav", sr, data.astype(np.int16))
    normalized_sound = normalize(data, -20.0)
    normalized_sound.export("./musicFiles/testHighNorm.wav", format = "wav")

def main():
    filename = sys.argv[1]
    sr, data = wavfile.read(filename)
    #sound = AudioSegment.from_file(filename, "wav")
    lowpass(sr, data)
    #highpass(sr, sound)

if __name__ == "__main__":
	main()
