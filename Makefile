CC=gcc

build:
	pip install --user scipy
	pip install --user numpy
	python -mpip install matplotlib
		
default: NotetakerGUI.py Notetaker.py chords.py duration.py file.py notes.py
	ln -s NotetakerGUI.py Notetaker

clean:
	rm Notetaker

