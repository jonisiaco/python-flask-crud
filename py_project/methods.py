from py_project import app
from flask.views import MethodView

class HttpMethod (MethodView):
	
	def get(self):
		return 'Get method'

	def post(self):
		return 'Post method'

	def put(self):
		return 'Put method'

	def delete(self):
		return 'Delete method'

app.add_url_rule('/request', view_func=HttpMethod.as_view('request') )
