from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
  apiKey: "AIzaSyDhpOFHB39VaPCWTmEW7Jyy3FoyPkmWWpc",
  authDomain: "jawad-9fd16.firebaseapp.com",
  projectId: "jawad-9fd16",
  storageBucket: "jawad-9fd16.appspot.com",
  messagingSenderId: "190357888489",
  appId: "1:190357888489:web:50cef14729a7a77debbf78",
  measurementId: "G-9K8NX1WR30"
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


app  = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.methods == 'POT':
     email = request.form['email']
     password = request.form['password']
     try: 
        login_session['user'] = auth.creat_user__with__email_and_password(email,password)
        return redirect(url_for('home'))
    except:
        error = "auth failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)