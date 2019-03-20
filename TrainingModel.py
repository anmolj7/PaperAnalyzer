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

Y = [] #Chapter
X = [] #Question

Questions = loadPickle('Pickles/Questions.pkl')

for x in Questions:
	for y in Questions[x]:
		Y.append(x+1)
		X.append(y)

documents = [] 

for x in range(len(X)):
	documents.append(preprocess_text(str(X[x])))

vectorizer = CountVectorizer(max_features=1200, min_df=6, max_df=0.85, stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(documents).toarray()

tfidC = TfidfTransformer()
X = tfidC.fit_transform(X).toarray()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

classifier = RandomForestClassifier(n_estimators=200, random_state=0)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

Print('')
print(classification_report(Y_test, Y_pred))
print(accuracy_score(Y_test, Y_pred))

savePickle(classifier, 'Pickles/Classifier.pkl')
savePickle(vectorizer, 'Pickles/Vectorizer.pkl')