from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk
import pymongo,logging,os

def preprocess(Text):
    Text = nltk.word_tokenize(Text)
    stemmer = PorterStemmer()
    stem = [stemmer.stem(word) for word in Text]
    words = [word for word in stem if word not in stopwords.words('english')]
    Text = " ".join(words)
    return Text


def DatabaseConn(News):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    dataBase = client["NewsArticle"]
    collection = dataBase["News_Article"]

    record = {"News" : News}
    collection.insert_one(record)

def log():
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
    log_dir = "running_logs/general_logs"
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(filename = os.path.join(log_dir,"running_logs.log"), level=logging.INFO, format=logging_str)
    
    