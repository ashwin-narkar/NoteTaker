#!/usr/bin/python

#notes are all relative to C3

''' notes = [('a0', 'a0'), ('as0', 'bb0'), ('b0', 'b0'),
        ('c1', 'c1'), ('cs1', 'db1'), ('d1', 'd1'), ('ds1', 'eb1'), ('e1', 'e1'), ('f1', 'f1'),
        ('fs1', 'gb1'), ('g1', 'g1'), ('gs1', 'ab1'), ('a1', 'a1'), ('as1', 'bb1'), ('b1', 'b1'),
        ('c2', 'c2'), ('cs2', 'db2'), ('d2', 'd2'), ('ds2', 'eb2'), ('e2', 'e2'), ('f2', 'f2'),
        ('fs2', 'gb2'), ('g2', 'g2'), ('gs2', 'ab2'), ('a2', 'a2'), ('as2', 'bb2'), ('b2', 'b2'),
        ('c3', 'c3'), ('cs3', 'db3'), ('d3', 'd3'), ('ds3', 'eb3'), ('e3', 'e3'), ('f3', 'f3'),
        ('fs3', 'gb3'), ('g3', 'g3'), ('gs3', 'ab3'), ('a3', 'a3'), ('as3', 'bb3'), ('b3', 'b3'),
        ('c4', 'c4'), ('cs4', 'db4'), ('d4', 'd4'), ('ds4', 'eb4'), ('e4', 'e4'), ('f4', 'f4'),
        ('fs4', 'gb4'), ('g4', 'g4'), ('gs4', 'ab4'), ('a4', 'a4'), ('as4', 'bb4'), ('b4', 'b4'),
        ('c5', 'c5'), ('cs5', 'db5'), ('d5', 'd5'), ('ds5', 'eb5'), ('e5', 'e5'), ('f5', 'f5'),
        ('fs5', 'gb5'), ('g5', 'g5'), ('gs5', 'ab5'), ('a5', 'a5'), ('as5', 'bb5'), ('b5', 'b5'),
        ('c6', 'c6'), ('cs6', 'db6'), ('d6', 'd6'), ('ds6', 'eb6'), ('e6', 'e6'), ('f6', 'f6'),
        ('fs6', 'gb6'), ('g6', 'g6'), ('gs6', 'ab6'), ('a6', 'a6'), ('as6', 'bb6'), ('b6', 'b6'),
        ('c7', 'c7'), ('cs7', 'db7'), ('d7', 'd7'), ('ds7', 'eb7'), ('e7', 'e7'), ('f7', 'f7'),
        ('fs7', 'gb7'), ('g7', 'g7'), ('gs7', 'ab7'), ('a7', 'a7'), ('as7', 'bb7'), ('b7', 'b7'),
        ('c8', 'c8')]
'''

notes = [("a,,,", "a,,,"), ("ais,,,", "bes,,,"), ("b,,,", "b,,,"),
        ("c,,", "c,,"), ("cis,,", "des,,"), ("d,,", "d,,"), ("dis,,", "ees,,"), ("e,,", "e,,"), ("f,,", "f,,"),
        ("fis,,", "ges,,"), ("g,,", "g,,"), ("gis,,", "aes,,"), ("a,,", "a,,"), ("ais,,", "bes,,"), ("b,,", "b,,"),
        ("c,", "c,"), ("cis,", "des,"), ("d,", "d,"), ("dis,", "ees,"), ("e,", "e,"), ("f,", "f,"),
        ("fis,", "ges,"), ("g,", "g,"), ("gis,", "aes,"), ("a,", "a,"), ("ais,", "bes,"), ("b,", "b,"),
        ("c", "c"), ("cis", "db"), ("d", "d"), ("dis", "eb"), ("e", "e"), ("f", "f"),
        ("fis", "ges"), ("g", "g"), ("gis", "aes"), ("a", "a"), ("ais", "bes"), ("b", "b"),
        ("c'", "c'"), ("cis'", "des'"), ("d'", "d'"), ("dis'", "ees'"), ("e'", "e'"), ("f'", "f'"),
        ("fis'", "ges'"), ("g'", "g'"), ("gis'", "aes'"), ("a'", "a'"), ("ais'", "bes'"), ("b'", "b'"),
        ("c''", "c''"), ("cis''", "des''"), ("d''", "d''"), ("dis''", "ees''"), ("e''", "e''"), ("f''", "f''"),
        ("fis''", "ges''"), ("g''", "g''"), ("gis''", "aes''"), ("a''", "a''"), ("ais''", "bes''"), ("b''", "b''"),
        ("c'''", "c'''"), ("cis'''", "des'''"), ("d'''", "d'''"), ("dis'''", "ees'''"), ("e'''", "e'''"), ("f'''", "f'''"),
        ("fis'''", "ges'''"), ("g'''", "g'''"), ("gis'''", "aes'''"), ("a'''", "a'''"), ("ais'''", "bes'''"), ("b'''", "b'''"),
        ("c''''", "c''''"), ("cis''''", "des''''"), ("d''''", "d''''"), ("dis''''", "ees''''"), ("e''''", "e''''"), ("f''''", "f''''"),
        ("fis''''", "ges''''"), ("g''''", "g''''"), ("gis''''", "aes''''"), ("a''''", "a''''"), ("ais''''", "bes''''"), ("b''''", "b''''"),
        ("c'''''", "c'''''")]

# fundamental frequencies of notes
frequencies = [27.0, 29.0, 30.0,
            32.0, 34.0, 36.0, 38.0, 41.0, 43.0, 46.0, 49.0, 51.0, 55.0, 58.0, 61.0,
            65.0, 69.0, 73.0, 77.0, 82.0, 87.0, 92.0, 98.0, 103.0, 110.0, 116.0,
            123.0, 130.0, 138.0, 146.0, 155.0, 164.0, 174.0, 185.0, 196.0, 207.0, 220.0,
            233.0, 246.0, 261.0, 277.0, 293.0, 311.0, 329.0, 349.0, 369.0, 392.0, 415.0,
            440.0, 466.0, 494.0, 523.0, 554.0, 587.0, 622.0, 659.0,
            698.0, 739.0, 783.0, 830.0, 880.0, 932.0, 987.0, 1046.0, 1108.0, 1174.0, 1244.0,
            1318.0, 1396.0, 1479.0, 1567.0, 1661.0, 1760.0, 1864.0, 1975.0, 2093.0, 2217.0, 2349.0,
            2489.0, 2637.0, 2793.0, 2959.0, 3135.0, 3322.0, 3520.0, 3729.0, 3951.0, 4186.0]

durations = []
noteDuration = ["8", "4." , "4", "2", "1"]

def durationsInit(bpm):
    secondsPerBeat = 60.0/bpm
    #Assume 4/4 time
    durations.append(secondsPerBeat/2)
    durations.append(secondsPerBeat*1.5)
    durations.append(secondsPerBeat)
    durations.append(secondsPerBeat*2)
    durations.append(secondsPerBeat*4)

def identifyDuration(dur):
    i=0
    index = 0
    minDiff = 100000
    while (i<len(durations)):
        diff = abs(durations[i] - dur)

        if (abs(diff) < minDiff):
            index = i
            minDiff = abs(durations[i] - dur)
        i+=1
    return noteDuration[index]

def identifyNote(freq):
    i=0
    while (i<len(frequencies) and frequencies[i] < freq):
        i+=1
    if (i == len(frequencies)-1):
        return -1
    if (i==0):
        return notes[0]
    if (frequencies[i] - freq > freq - frequencies[i-1]):
        i-=1
    return notes[i][0]
