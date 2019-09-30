from flask import Flask
from config import Config
from mysqlc import Mysql

#Flask project
app = Flask(__name__, instance_relative_config=True)

#SECRET_KEY
app.config.from_object(Config)

#Database Connection
db = Mysql(host='127.0.0.1', user='root', password='root', database='py_project')

#View Controllers
import py_project.index
import py_project.signin
import py_project.news
import py_project.methods