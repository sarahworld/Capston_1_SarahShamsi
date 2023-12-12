from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired


class ProductForm(FlaskForm):

    upc_code = StringField('UPC/Barcode', validators=[InputRequired()])

