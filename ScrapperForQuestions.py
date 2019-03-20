import re
from Modules.Functions import * 

#Url which contains links to all the chapters' import questions.. 
base_url = "https://www.cbsetuts.com/chapter-wise-important-questions-class-10-mathematics/"
soup = getSoup(base_url)

#Scrapping For The Links, Along With The Names Of Chapters.. 
OL = soup.find('ol')
LI = OL.findAll('li')
Links = []
ChapterNames = {}

count = 0
for x in LI:
	a = x.find('a')
	x = x.text.split()[4:]
	ChapterNames[count] = ' '.join(x)
	Links.append(a.get('href'))
	count += 1 

Questions = {}
savePickle(ChapterNames, 'Pickles/Chapters.pkl')
Print('Chapters Scrapped.')

for chap_num, link in enumerate(Links):
	Questions[chap_num] = [] 
	soup = getSoup(link)
	Q = []
	P = soup.findAll('p')
	P = P[3:]
	pattern = r'Question [0-9]{,3}\.\n'
	for x in P:
		if re.search(pattern, x.text, 0):
			x = x.text 
			x = re.sub(pattern, '', x)
			x = re.split('Solution|Answer:', x)[0] #Selecting only the questions.
			x = x.replace('\n', ' ').strip()
			if not x.isspace():
				Q.append(x)
	Questions[chap_num] = Q 
	Print(link)
Print('Questions Scrapped.')
savePickle(Questions, 'Pickles/Questions.pkl')
Print('Pickles/Questions.pkl Dumped.')
