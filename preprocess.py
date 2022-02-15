from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk

def preprocess(Text):
    Text = nltk.word_tokenize(Text)
    stemmer = PorterStemmer()
    stem = [stemmer.stem(word) for word in Text]
    words = [word for word in stem if word not in stopwords.words('english')]
    Text = " ".join(words)
    return Text