"""View functions - includes all handlers"""

from flask import render_template, flash, redirect
from app import app

from forms import LoginForm


@app.route("/")

@app.route('/index')
def index():
	user = { 'nickname': 'Miguel'} # fake user

	posts = [# fake array of posts
		{
			'author': { 'nickname': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{	'author': { 'nickname': 'Susan'},
			'body':	'The Avengers movie was so cool!'
		}
		]
	return render_template("index.html", 
						title = "home",
						user = user,
						posts = posts)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm() # instantiates form object
	#LoginForm class defined in forms.py

	if form.validate_on_submit(): # validate on submit is a built-in method for Form class in WTF
		flash('Login requested for OpenID="' + form.openid.data + '" , remember_me=' + str(form.remember_me.data))
		# flash function imported from Flask
		return redirect('/index')
	
	return render_template('login.html',
						title = 'Sign In',
						form = form,
						providers = app.config['OPENID_PROVIDERS']
						)


if __name__ == "__main__":
    app.run(debug = True)