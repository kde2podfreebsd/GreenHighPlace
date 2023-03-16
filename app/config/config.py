import os
import configparser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


config = configparser.ConfigParser()
basedir = os.path.abspath(os.path.dirname(__file__))
config.read(f"{basedir}/../../config.ini")

DB_SETTINGS = {
    'host': config['POSTGRESQL_DATABASE']['host'],
    'port': config['POSTGRESQL_DATABASE']['port'],
    'database': config['POSTGRESQL_DATABASE']['database'],
    'user': config['POSTGRESQL_DATABASE']['user'],
    'password': config['POSTGRESQL_DATABASE']['password']
}

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL",
                                                  f"postgresql://root:root@{DB_SETTINGS.get('host')}:5432/{DB_SETTINGS.get('database')}")
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
