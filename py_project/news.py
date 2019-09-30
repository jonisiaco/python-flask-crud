from py_project import app, db
from flask import render_template, redirect, url_for, flash, session

def home():
	if sessionExist():
		return render_template('news.html', news=getNews())
	else:
		return redirect(url_for('index'))

@app.route("/news/<int:id>")
def details(id):
	return render_template('details.html', id=id, data=getNewsByID(id))


def sessionExist():
	if 'username' not in session:
		return False
	return True

def getNews():
	mysql = db._open(prepared=False, dictionary=True)
	q = """SELECT id, title, content, updated_at, created_at FROM news LIMIT 0,10"""
	mysql.execute(q)
	data = mysql.fetchall()
	db._close()
	return data

def getNewsByID(id):
	mysql = db._open(prepared=True, dictionary=True)
	q = """SELECT id, title, content, updated_at, created_at FROM news WHERE id = %s"""
	mysql.execute(q,(id,))
	data = mysql.fetchone()
	db._close()
	return data

app.add_url_rule('/news', 'news_index', home)