from flask import Flask, render_template, redirect, request, jsonify
import requests
import os

from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db
from forms import ProductForm
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
client = OpenAI()
load_dotenv()

app.config['SECRET_KEY'] = 'Its a secret!';
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///product_descriptor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
app.config['SQLALCHEMY_ECHO'] = True;

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False;

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

barcode_api_key = os.environ.get("BARCODE_API_KEY")

@app.route('/')
def index():
    form = ProductForm()
    return render_template('home.html',page_title='Home',form=form)

@app.route('/search', methods=['GET','POST'])
def search():
    form = ProductForm()

    if form.validate_on_submit():
        upc_code = form.upc_code.data;
        response = requests.get(f'https://api.barcodelookup.com/v3/products?barcode={upc_code}&formatted=y&key={barcode_api_key}')
        result = response.json().get("products")
        for item in result:
            product_name = item['title']
            product_image = item['images']
   
        # product_name='Oreo Thins Original Sandwich Cookies, 1 Resealable Pack (287G)'

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
      
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"What is the country of origin of {product_name}?Give one word answer.Is it vegetarian or not? Give your confidence percentage? Give two words answer."}]
        )
        # print(completion.choices[0].message)
        description= completion.choices[0].message
        print(description)

        return render_template('result.html',page_title="result", result=result, description=description)

   
    return render_template('home.html', page_title='Home', form=form)
    
    
   


