from py_project import app
from flask import render_template, session
from flask.views import MethodView

class Index(MethodView):

	def dispatch_request(self):
		username = session['username'] if 'username' in session else ""
		user = {'username': username}
		return render_template('index.html', title='Home', user=user)

app.add_url_rule("/", view_func=Index.as_view('index'))

