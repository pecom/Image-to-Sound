# Image-to-Sound
Convert images to "music"!

A simple program I made at HackNC that takes images and changes them to a .wav file.

The program uses PIL and pysynth so those need to be installed for the program to run. If you want to change which image
is being converted, go to the .py file and change the line:

testImage = Image.open("10test.png");

to: testImage = Image.open(imageNameHere);

The image must be in the same directory as the program. 

PIL: https://pillow.readthedocs.org/installation.html
pysynth: http://mdoege.github.io/PySynth/

*The .wav files are huge and big pictures take a veryyyyyyy long time to run. The program is pretty inefficient since it turns every pixel into a note, so a 10x10 px picture has 100 notes...*
