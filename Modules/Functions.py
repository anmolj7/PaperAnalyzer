import operator
import textract 
from nltk import word_tokenize, pos_tag 
import os 
from nltk.stem import WordNetLemmatizer 
import pickle 
import nltk, re 
import urllib
import string
from bs4 import BeautifulSoup


def savePickle(data, FILE):
	pickle.dump(data, open(FILE, 'wb'))

def loadPickle(path):
	return pickle.load(open(path, 'rb'))

def breakLine(num=55):
	print("*"*num)

def Print(*string):
	print(*string)
	temp = len(''.join(string)) 
	if len(str(temp))>1:
		x = len(''.join(string)) 
	else:
		x = 55 
	breakLine(x)

def getSoup(url):
    HDR = {'User-Agent':'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=HDR)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, "lxml")
    return soup

def preprocess_text(document):
	stemmer = WordNetLemmatizer() #Lemmatizier is Converting Words To Their Dictionary Forms.. For example, Picks to pick.
	# Remove all the special characters
	document = re.sub(r'\W', ' ', document)
	# remove all single characters
	document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
	# Remove single characters from the start
	document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
	# Substituting multiple spaces with single space
	document = re.sub(r'\s+', ' ', document, flags=re.I)
	# Removing prefixed 'b'
	document = re.sub(r'^b\s+', '', document)
	# Converting to Lowercase
	document = document.lower()
	# Lemmatization
	document = document.split()
	document = [stemmer.lemmatize(word) for word in document]
	document = ' '.join(document)
	return document

def clean_text(text):
	'''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
	text = text.lower()
	text = text.replace('\\n', ' ')
	text = re.sub('\[.*?\]', ' ', text)
	text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
	text = re.sub('\w*\d\w*', ' ', text)
	return text

def SortDict(Dict):
	'''Function For Sorting A Dict In a non decreasing order.'''
	Temp = sorted(Dict.items(), key=operator.itemgetter(1), reverse=True)
	return {x:y for x,y in Temp}
