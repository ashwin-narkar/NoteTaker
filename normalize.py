#!/usr/bin/python3
import sys
import numpy as np
from pydub import AudioSegment

def normalize(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

sound = AudioSegment.from_file("./musicFiles/Africa.wav", "wav")
normalized_sound = normalize(sound, 10.0)
normalized_sound.export("./musicFiles/nomrmalizedAudio.wav", format="wav")
