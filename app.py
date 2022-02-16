from flask import Flask,render_template,request
import re
import pickle
from utils import preprocess,DatabaseConn

app = Flask(__name__)

classifier = pickle.load(open('model/model.pkl', 'rb'))
cv = pickle.load(open('model/transform.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == "POST":
        Text = request.form['article']
        DatabaseConn(News=Text)
        preprocessed_text = preprocess(Text)
        vect = cv.transform([preprocessed_text])
        my_prediction = classifier.predict(vect)

        return render_template("welcome.html", score = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)