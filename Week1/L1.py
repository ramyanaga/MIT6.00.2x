import pylab
import numpy as np
def loadFile():
	inFile = open("julyTemps.txt")
	highs = []
	lows = []
	for line in inFile: 
		fields = line.split()
		if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
			continue
		else:
			highs.append(fields[1])
			lows.append(fields[2])
	#print type(lows), type(highs)
	return (lows,highs)


def producePlot(lowTemps, highTemps):
	diffTemps = []
	for i in range(0,31):
		diffTemps.append(int(highTemps[i])-int(lowTemps[i]))
	diffTemps = list(np.array(diffTemps))
	pylab.title('Day by Day Ranges in Temperature in Boston'
		+ 'in July 2012')
	pylab.xlabel('Days')
	pylab.ylabel('Temperature Ranges')
	pylab.plot(range(1,32), diffTemps)
	pylab.show()

(lowTemps, highTemps) = loadFile()
producePlot(lowTemps, highTemps)

