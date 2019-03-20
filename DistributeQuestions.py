from Modules.Functions import * 
from predict import predict 
import os 
import pickle

Chapters = loadPickle('Pickles/Chapters.pkl')
Distributed = {Chapters[x]:{y:[] for y in range(1, 5)} for x in Chapters}

files = os.listdir(os.getcwd()+'/Papers')
files = [x for x in files if '.pkl' in x]

def DistributeQuestions(paper_pkl):
	Paper = loadPickle(paper_pkl)
	_Distributed = {Chapters[x]:{y:[] for y in range(1, 5)} for x in Chapters}
	#These All Are Metrics For Weighing Questions According to Papers.
	if len(Paper) == 34:
		ONE = list(range(1, 11))
		TWO = list(range(11, 19))
		THREE = list(range(19, 30))
		FOUR = list(range(30, 35))
	if len(Paper) == 31:
		ONE = list(range(1, 5))
		TWO = list(range(5, 11))
		THREE = list(range(11, 20))
		FOUR = list(range(20, 32))
	if len(Paper) == 30:
		ONE = list(range(1, 7))
		TWO = list(range(7, 13))
		THREE = list(range(13, 23))
		FOUR = list(range(23, 31))
	for x, y in enumerate(Paper):
		Chapter = Chapters[predict(y)-1]
		if x in ONE:
			_Distributed[Chapter][1] += y.split('OR')
		if x in TWO:
			_Distributed[Chapter][2] += y.split('OR')
		if x in THREE:
			_Distributed[Chapter][3] += y.split('OR')
		if x in FOUR:
			_Distributed[Chapter][4] += y.split('OR')
	return _Distributed	

if __name__ == '__main__':
	for f in files:
		f = 'Papers/' + f 
		Temp = DistributeQuestions(f)
		for x in Temp:
			for y in Temp[x]:
				Distributed[x][y] += Temp[x][y]
		Print(f)
	savePickle(Distributed, 'Pickles/Distributed.pkl')
	Print('Pickles/Distributed.pkl Dumped.')