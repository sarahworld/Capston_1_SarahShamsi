from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app;
    db.init_app(app);

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    upc_code = db.Column(db.String(),
                         nullable=False)
    
    name = db.Column(db.String(),
                     nullable=False)
    
    image_url = db.Column(db.String(),
                          nullable=True)
    
    description = db.Column(db.String(),
                          nullable=True)
    






