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
    
    @classmethod
    def create_product(cls, name, upc_code, image_url, description):

        product = Product(
                    upc_code=upc_code,
                    name=name,
                    image_url=image_url,
                    description=description
        )

        db.session.add(product)
        db.session.commit()

        return product

class Questions(db.Model):
    __tablename__ = "questions"


    product_id = db.Column(db.Integer(),
                           db.ForeignKey('products.id'),
                           primary_key=True)
    
    origin_country = db.Column(db.String())

    is_vegetarian = db.Column(db.String())

    confidence_percentage = db.Column(db.String());

    product = db.relationship("Product");


    @staticmethod
    def serialize_product_questions(questions):
        print("Line 62", questions);
        print(type(questions))
        
        return questions

    def get(self,upc_code):
        product = Product.query.filter_by(upc_code=upc_code).first();
        print("PPPPPPPPPPPP",product)
        product_id = product.id;

        product_questions = Questions.query.filter_by(product_id=product_id).first();
        print("LINE 75", product_questions);
        if product_questions:
            return self.serialize_product_questions(product_questions)
        
        return None
    
    @classmethod
    def create_questions(cls, product_id, origin_country,is_vegetarian,confidence_percentage):

        questions = Questions(
                        product_id=product_id,
                        origin_country=origin_country,
                        is_vegetarian=is_vegetarian,
                        confidence_percentage=confidence_percentage
        )

        db.session.add(questions);
        db.session.commit()

        return questions

        





