from py_project import app, db
from forms import LoginForm
from flask import render_template, redirect, url_for, flash, session

@app.route('/signin', methods=["GET", "POST"])

def login():
	form = LoginForm()

	if form.validate_on_submit():

		user_name = form.username.data
		password = form.password.data

		if authUser(user_name, password):
			session['username'] = user_name
			return redirect(url_for('news_index'))

	#flash('custom message')
	return render_template('signin.html', form=form)

@app.route('/logout')  

def logout():
	if 'username' in session:
		session.pop('username',None)  
	
	return redirect(url_for('index'))

def authUser(user_name, password):
	token = 'secret'
	mysql = db._open(prepared=True, dictionary=False)
	q1 = """SELECT id, name, AES_DECRYPT(pass, %s) pass FROM user WHERE name = %s"""
	mysql.execute(q1,(token, user_name))
	data = mysql.fetchone()
	db._close()

	if data == None:
		return False

	if str(data[2]) != str(password):
		return False

	return data


