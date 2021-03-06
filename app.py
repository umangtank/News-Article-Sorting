from flask import Flask,render_template,request
import pickle,logging,os
from utils.all_utils import preprocess,DatabaseConn,log,read_config

app = Flask(__name__)

config = read_config()

model = config["model"]["model_dir"]
model_path = os.path.join(model,config["model"]["model_file"])
transform_file = os.path.join(model,config["model"]["tfidf_file"])

classifier = pickle.load(open(model_path, 'rb'))
cv = pickle.load(open(transform_file,'rb'))


@app.route('/')
def home():
    logging.info("Home Page")
    return render_template("index.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
    logging.info("Submit Page")
    if request.method == "POST":

        Text = request.form['article']
        logging.info("Text: " + Text)
        DatabaseConn(News=Text)
        
        logging.info("Database Connection")
        preprocessed_text = preprocess(Text)
        vect = cv.transform([preprocessed_text])
        my_prediction = classifier.predict(vect)


        logging.info("Prediction: " + str(my_prediction))
        logging.info("rendering welcome.html")
        return render_template("welcome.html", score = my_prediction)

if __name__ == '__main__':
    log()
    logging.info("Server is running")
    logging.info("Start predicting")
    app.run(debug=True) 