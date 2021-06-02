from flask import Flask, redirect, url_for, request
from main import *
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'the tweet is %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      score1 = classify_tweet(user)
      return redirect(url_for('success',name = score1))
   else:
      user = request.args.get('nm')
      score1 = classify_tweet(user)
      return redirect(url_for('success',name = score1))


if __name__ == '__main__':
   app.run(debug = True)