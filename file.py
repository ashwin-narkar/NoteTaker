#!/usr/bin/python

def startFile():
		f = open("sheet.ly", "a")
		f.truncate(0)
		f.write("\\version " + "\"" + "2.18.2" + "\"" + "\n")
		f.write("{\n")
		f.close()

def writeToFile(notes):

	f = open("sheet.ly", "a")
	i=0
	while (i < len(notes)-1):
		f.write(notes[i]) 	#writes notes
		i += 1
		f.write(notes[i])	#writes durations of notes
		i += 1
		f.write(" ")
	f.write(notes[i])
	f.write("4")
	f.write(" ")

	f.close()

def endFile():
		f = open("sheet.ly", "a")
		f.write("\n}")
		f.close()
