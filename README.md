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
