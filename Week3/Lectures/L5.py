import math
import random
"""
def noReplacementSimulation(numTrials):
	bucket = ['red','green','red','green','red','green']
	drawn = []
	threeBallProb = 0
	for trial in range(numTrials):
		bucket = ['red','green','red','green','red','green']
		drawn = []
		choice1 = random.randint(0,5)
		drawn.append(bucket[choice1])
		bucket.insert(choice1,'nothing')
		choice2 = random.randint(0,4)
		while bucket[choice2] == 'nothing':
			choice2 = random.randint(0,4)
		drawn.append(bucket[choice2])
		bucket.insert(choice2,'nothing')
		choice3 = random.randint(0,3)
		while bucket[choice3] == 'nothing':
			choice3 = random.randint(0,3)
		drawn.append(bucket[choice3])
		bucket.insert(choice3,'nothing')
		if drawn[0] == drawn[1] and drawn[1] == drawn[2]:
			threeBallProb+=1
		#print drawn
	return float(float(threeBallProb)/float(numTrials))
	"""
def noReplacementSimulation(numTrials):
	bucket = ['red','green','red','green','red'',green']
	drawn = []
	threeBallProb = 0
	for trial in range(numTrials):
		bucket = ['red','green','red','green','red','green']
		drawn = []
		choice1 = random.randint(0,5)
		drawn.append(bucket[choice1])
		bucket.remove(bucket[choice1])
		#print bucket
		choice2 = random.randint(0,4)
		drawn.append(bucket[choice2])
		bucket.remove(bucket[choice2])
		choice3 = random.randint(0,3)
		drawn.append(bucket[choice3])
		bucket.remove(bucket[choice3])
		if drawn[0] == drawn[1]:
			if drawn[1] == drawn[2]:
				threeBallProb+=1
	return float(float(threeBallProb)/float(numTrials))


print noReplacementSimulation(10000)

