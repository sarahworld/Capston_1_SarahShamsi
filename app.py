from flask import Flask, render_template, redirect, request, jsonify

import os
from openAICapstone import OpenAICapstone
from barcodeCapstone import BarcodeCapstone

from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Product, Questions
from forms import ProductForm

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
def index():
    form = ProductForm()
    return render_template('home.html',page_title='Home',form=form)

@app.route('/search', methods=['GET','POST'])
def search():
    form = ProductForm()

    if form.validate_on_submit():
        upc_code = form.upc_code.data;
        # Check in the product if this upc code exists
        product = Product.query.filter_by(upc_code=upc_code).first();
        print("Line 39",product)

        if not product:
            barcode = BarcodeCapstone()
            barcode_dict = barcode.call(upc_code=upc_code)

            # Create product in DB
            product = Product.create_product(upc_code=upc_code,name=barcode_dict['name'],image_url=barcode_dict['image'],description=None);
        
        
        product_upc = product.upc_code;
        print(product_upc)

        product_name = product.name;
        print("Line 50")

        questions = Questions()
        content = questions.get(upc_code)
        print("LINE 55",content);
       
        if not content:
            # if content not available call open ai
            ai = OpenAICapstone()
            content = ai.call(product_name=product_name)
            print("CCCCCCCCCCCCC",content)

            # Create questions in DB
            questions = Questions.create_questions(product_id=product.id,origin_country=content['origin_country'],is_vegetarian=content['is_vegetarian'],confidence_percentage=content['confidence_percentage'])

        return render_template('result.html',page_title="result", product=product, content=content)
        # return {'content':content}   

    return render_template('home.html', page_title='Home', form=form)
    
    
   


