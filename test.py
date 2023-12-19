
import unittest
from app import app
from unittest import TestCase
from models import db

app.config['TESTING'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///product-test"
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all();

class testing(TestCase):

    def setUp(self):
        """Create test client and add sample data"""
      
        self.client = app.test_client(self)

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
        
    def test_home_page(self):
        
        resp = self.client.get('/');
        # html= resp.get_data(as_text=True);
     
        self.assertEqual(resp.status_code, 200);
        self.assertIn(b'PRODUCT DESCRIPTOR',resp.data);

    


if __name__ == '__main__':
    unittest.main();