from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "roni"
password = "1324"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi","Alma","Daria","Shiri","Mjd","Yoav","Jan"]


@app.route('/login',methods=['GET','POST'])  # '/' for the default page
def login():
  if request.method == 'POST':
       username1 = request.form['username']
       password1 = request.form['password']
       if username==username1 and password==password1:
            return render_template('home.html', names = facebook_friends)
       else:
            return render_template('login.html')
  return render_template('login.html')
    
@app.route('/home')
def home():
     return render_template('home.html')
  
@app.route('/friend_exists/<string:name>')
def hello_name_route(name):
    return render_template('friend_exists.html', n = name in facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
