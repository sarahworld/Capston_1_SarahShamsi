import requests
import os 

from dotenv import load_dotenv
load_dotenv()

class BarcodeCapstone:
    def __init__(self) -> None:
        self.barcode_api_key = os.environ.get("BARCODE_API_KEY")
        
    def call(self, upc_code):

        response = requests.get(f'https://api.barcodelookup.com/v3/products?barcode={upc_code}&formatted=y&key={self.barcode_api_key}')
        result = response.json().get("products")
        for item in result:
            product_name = item['title']
            product_image = item['images'][0]
        

        return {'name':product_name, 'image':product_image}
        