from Modules.Functions import * 
import pickle 
import textract
import re 


Links = ['https://www.topperlearning.com/study/cbse/class-10/mathematics/previous-year-question-papers/55560/pdf/b101c2s3e8',
	   'https://www.topperlearning.com/study/cbse/class-10/mathematics/previous-year-question-papers/55554/pdf/b101c2s3e8',
	   'https://www.topperlearning.com/study/cbse/class-10/mathematics/previous-year-question-papers/53477/pdf/b101c2s3e8',
	   'https://www.topperlearning.com/study/cbse/class-10/mathematics/previous-year-question-papers/52441/pdf/b101c2s3e8']

file = 'Papers/Paper{}.{}'

for i, url in enumerate(Links):
	#Extracting Questions.
	soup = getSoup(url)
	div = soup.find('div', attrs={'class':'sampleContainer'})

	text = div.text 
	text = text.split('''Download PDF\n\n\n\nExplore CBSE Class 10 Mathematics''')[0]
	if i == 0:
		text = re.split(r'Q\.? [0-9]{,2}\.?', text)
	else:
		text = re.split(r'Q\.? [0-9]{,2}\.', text)
	text = [x.encode('ascii', 'ignore').decode('utf-8') for x in text]
	text = [preprocess_text(x) for x in text]
	text = [x for x in text if x] #Checking if x is not empty 
	
	if i == 0:
		text[6] += text.pop(7)
		text[13] += text.pop(14)
	text[-1] = text[-1].split('''download pdf explore cbse class 10 mathematics previous year question paper cbse class 10 mathematics previous year question paper 2019 all india set 3 question solution cbse class 10 mathematics previous year question paper 2017''')[0]
	savePickle(text, ''+file.format(i+1, 'pkl'))
	Print('{} Dumped.'.format(file.format(i+1, 'pkl')), str(len(text)))

def returnText(X):
	text = ''.join(X[1:])
	text = text.replace('www.topperlearning.com', '')
	re.sub(r'Question numbers [0-9]{,2} to [0-9]{,2} carry [0-9] mark each.', '', text)
	text = text.replace('CBSE X | Mathematics', '')
	text = text.replace('Board Paper 203 2012', '')
	text = re.sub(r'\[[0-9]\]', '', text)
	text = text.split('\\n')
	text = [x for x in text if len(x)>1]
	return text 

#Extracting Questions From PDF Files...
for i in range(5, 9):
	Paper = textract.process(file.format(i, 'pdf'))
	Paper = str(Paper).encode('ascii', 'ignore').decode('utf-8')
	Paper = Paper.replace('CBSE X | Mathematics\\nBoard Paper 2012\\n\\nCBSE Board', "")
	Paper = re.sub(r'(\\xc3)?(\\xa2)?(\\xc2)?(\\x80)?(\\xc2)?(\\x93)?(\\xe2)?', '', Paper)
	Paper = re.sub(r'\\x\w', '', Paper)
	if Paper:
		X = re.split(r'SECTION  ?[ABCD]?', str(Paper))
		X = returnText(X)
		temp = []
		for y in X:
			temp.append(re.findall(r'([0-9]{,2})\.', y))
		prevNumber = 0 
		initId = 0 
		Paper = [] 
		ques = ""
		for x in range(len(X)):
			try:
				if prevNumber+1 == int(temp[x][0]):
					ques = ' '.join(X[initId:x])
					Paper.append(ques)
					initId = x 
					prevNumber += 1 
			except:
				pass
		ques = ' '.join(X[initId:x])
		Paper.append(ques)
	Paper = Paper[1:]
	savePickle(Paper, file.format(i, 'pkl'))
	Print("{} Dumped.".format(file.format(i, 'pkl')), str(len(Paper)))