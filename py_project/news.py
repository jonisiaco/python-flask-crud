from py_project import app, db
from flask import render_template, redirect, url_for, flash, session
from datetime import date, datetime, timedelta
from forms import Edit

def home():
	if sessionExist():
		return render_template('news.html', news=getNews())
	return redirect(url_for('index'))

@app.route("/news/<int:id>")
def details(id):
	if not sessionExist():
		return redirect(url_for('index'))

	news = getNewsByID(id)
	data = {}
	for n in news:
		data[n] = news[n]
		if n == 'content':
			data[n] = nl2br(news[n])

	return render_template('details.html', id=id, data=data)

@app.route("/news/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
	if not sessionExist():
		return redirect(url_for('index'))

	form = Edit()
	if form.validate_on_submit():
		data = {
			'id' : form.id.data,
			'title' : form.title.data,
			'content' : form.content.data
		}
		insert( data )

		return redirect(url_for('news_index'))

	return render_template('edit.html', data=getNewsByID(id), form=form)


def sessionExist():
	if 'username' not in session:
		return False
	return True

def getNews():
	mysql = db._open(dictionary = True)
	q = """SELECT id, title, content, updated_at, created_at FROM news LIMIT 0,10"""
	mysql.execute(q)
	data = mysql.fetchall()
	db._close()
	return data

def getNewsByID(id):
	mysql = db._open(dictionary = True)
	q = """SELECT id, title, content, updated_at, created_at FROM news WHERE id = %s"""
	mysql.execute(q,(id,))
	data = mysql.fetchone()
	db._close()
	return data

def insert(data):
	mysql = db._open()
	now = str(datetime.now())

	if 'id' in data :
		q = ("UPDATE news SET title = %s, content = %s WHERE id = %s")
		values = (data['title'], data['content'], data['id'] )

	else:	
		q = ("INSERT INTO news (title, content, created_at) VALUES (%s, %s, %s)")
		values = ( data['title'], data['content'], now )

	mysql.execute(q,values)
	db._commit()
	db._close()


def nl2br(s):
	return s.replace('\n','<br />\n')


app.add_url_rule('/news', 'news_index', home)