# -*- encoding: utf-8 -*-


from flask import Blueprint
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'dbname'

mysql = MySQL(app)


blueprint = Blueprint(
    'checker',
    __name__,
    url_prefix=''
)
