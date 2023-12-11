from flask import Flask, render_template, redirect, request

from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Its a secret!';
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///product_descriptor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
app.config['SQLALCHEMY_ECHO'] = True;

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False;

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    return render_template('base.html')