from app import app
from models import db, Product, Questions

db.drop_all();
db.create_all();

p1 = Product(upc_code="060383041168",name="Medium Roast Coffee",image_url="https://images.barcodelookup.com/57850/578500009-1.jpg",description="Food, Beverages & Tobacco");
p2 = Product(upc_code="068721002512",name="Dempster's Dempster S 100% Whole Wheat Brea",image_url="https://dempsters.ca/sites/default/files/styles/large/public/2023-04/BC_121899_DEM_Whole%20Wheat_675g-1222_A1N1.png?itok=8TmedNul",description="Food, Beverages & Tobacco");
p3 = Product(upc_code="627735012971", name="Great Value Iodized Fine Sea Salt",image_url="https://images.barcodelookup.com/66634/666343688-1.jpg",description="Food, Beverages & Tobacco");

db.session.add(p1);
db.session.add(p2);
db.session.add(p3);

db.session.commit();

coffee_questions=Questions(product_id=1,origin_country="Brazil",is_vegetarian=True,confidance="90%");
Bread_questions=Questions(product_id=2,origin_country="Canada",is_vegetarian=True,confidance="95%");
Salt_questions=Questions(product_id=3,origin_country="USA",is_vegetarian=True,confidance="80%");

db.session.add(coffee_questions);
db.session.add(Bread_questions);
db.session.add(Salt_questions);

db.session.commit();