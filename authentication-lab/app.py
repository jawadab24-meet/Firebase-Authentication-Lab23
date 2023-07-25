from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
  "apiKey": "AIzaSyDhpOFHB39VaPCWTmEW7Jyy3FoyPkmWWpc",
  "authDomain": "jawad-9fd16.firebaseapp.com",
  "projectId": "jawad-9fd16",
  "storageBucket": "jawad-9fd16.appspot.com",
  "messagingSenderId": "190357888489",
  "appId": "1:190357888489:web:50cef14729a7a77debbf78",
  "measurementId": "G-9K8NX1WR30",
  "databaseURL":"https://jawad-9fd16-default-rtdb.firebaseio.com/",
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app  = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signin():
    # if request.method == 'POST':
        
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user={"email" : request.form['email'],"bio" : request.form['bio']}
        #try: 
        login_session['user'] = auth.create_user_with_email_and_password(user["email"],request.form['password'])
        uid= login_session['user']['localId']
        db.child("user").child(uid).set(user)
        return redirect(url_for('add_tweet'))
        #except:
           # error = "auth failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        try:
            uid= login_session['user']['localId']
            tweet = {"title" : request.form['title'], "tweet": request.form['tweet'], "uid":uid}
            db.child("Tweets").push(tweet)
            return redirect(url_for('all_tweet'))
        except:
            error = "Tweet error, please try again"
            return render_template("add_tweet.html", error_msg = error)
    else:
        return render_template('add_tweet.html')


@app.route('/all_tweets')
def all_tweet():
    all_tweet1 = db.child("tweet").get().val()
    return render_template("tweets.html" , all_tweet=all_tweet1)


if __name__ == '__main__':
    app.run(debug=True)