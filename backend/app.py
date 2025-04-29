from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[DANE_KNIGHT]'
db = SQLAlchemy(app)

engine = create_engine('postgresql://localhost/[DANE_KNIGHT]')