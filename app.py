


from textblob import TextBlob 
from textblob.sentiments import NaiveBayesAnalyzer

from flask import Flask, render_template , request


app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
  return render_template("index.html")



# *******Sentence level sentiment analysis
@app.route("/predict1", methods=['POST','GET'])
def pred1():
	if request.method=='POST':
            text = request.form['txt']
            blob = TextBlob(text)
            if blob.sentiment.polarity > 0:
                text_sentiment = "positive"
            elif blob.sentiment.polarity == 0:
                text_sentiment = "neutral"
            else:
                text_sentiment = "negative"
            return render_template('result1.html',msg=text, result=text_sentiment)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)

