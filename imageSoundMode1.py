from PIL import Image
import pysynth


testImage = Image.open("PoM300.png");

noteNameDict = { '0': 'a', '1': 'a#', '2': 'b', '3': 'c',
		 '4': 'c#', '5': 'd', '6': 'd#', '7': 'e',
		'8': 'f', '9': 'f#', '10': 'g', '11': 'g#' }

noteList = []

def numNote(n):
	"Assigns a number to a pitch"
	return noteNameDict[str(n % 12)]

def numOct(n):
	"Assigns a number to an octave"
	if (n < 4):
		return '0'
	elif( n == 255):
		return '8'
	else:
		return list(str(((n-3)//36)+1))[0]

def numNoteOct(n, m):
	"Combines numNote and numOct"
	return numNote(n) + str(numOct(m))

def numLength(n):
	"Assigns a number to a note length"
	a = n//16
	if( a == 0):
		return 8
	elif( a == 1):
		return 12
	elif( a == 3 or a == 2):
		return 16
	elif( a == 5 or a == 4):
		return 8
	elif( a > 5 and a < 10):
		return 4
	elif( a == 10 or a == 11):
		return 8
	elif( a == 12 or a == 13):
		return 12
	elif( a == 14):
		return 2
	elif( a == 15):
		return 1
	else:
		return 4

for i in range(testImage.size[0]):
	for j in range(testImage.size[1]):
		r, g, b = testImage.getpixel( (i,j) )
		noteList.append( (numNoteOct(r, g), numLength(b)) )

imageSound = tuple(noteList)
pysynth.make_wav(imageSound, fn = "mode1.wav")
