from Modules.Functions import *
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Nothing Necessary To Comment About.

vectorizer = loadPickle('Pickles/Vectorizer.pkl')
classifier = loadPickle('Pickles/Classifier.pkl')

def predict(String):
	S = preprocess_text(String)
	S = clean_text(S)
	X = vectorizer.transform([S]).toarray()
	return classifier.predict(X)[0]