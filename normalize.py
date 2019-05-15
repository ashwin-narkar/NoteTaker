#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment

def normalize(soundfile, target_dBFS):
    sound = AudioSegment.from_file(soundfile, "wav")
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

#normalized_sound = normalize(sound, -20.0)
#normalized_sound.export("./musicFiles/nomrmalizedAudio.wav", format="wav")
