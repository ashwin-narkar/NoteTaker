#!/usr/bin/python

def startFile():
		f = open("sheet.ly", "a")
		f.truncate(0)
		f.write("\\version " + "\"" + "2.18.2" + "\"" + "\n")
		f.write("{\n")
		f.close()

def writeToFile(note):
	f = open("sheet.ly", "a")
	f.write(note)
	f.write(" ")
	f.close()

def endFile():
		f = open("sheet.ly", "a")
		f.write("\n}")
		f.close()
