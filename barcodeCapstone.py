import requests
import os 


from dotenv import load_dotenv
load_dotenv()

class BarcodeCapstone:
    def __init__(self) -> None:
        self.barcode_api_key = os.environ.get("BARCODE_API_KEY")
        
    def call(self, upc_code):

        try:
            # Check for API key is available
            if not self.barcode_api_key:
                raise ValueError("Barcode_api_key is not set in environtment variable")
            
            # Make the API request  
            response = requests.get(f'https://api.barcodelookup.com/v3/products?barcode={upc_code}&formatted=y&key={self.barcode_api_key}')
            response.raise_for_status()      # Raise HTTP error for bad responses

            # Parse the response
            result = response.json().get("products")

            if not result:
                raise ValueError(f"No product found for provided UPC Code: {upc_code}")
            
            # Extract product details
            for item in result:
                product_name = item['title']
                product_image = item['images'][0]
                return {'name':product_name, 'image':product_image}
        
        except requests.exceptions.RequestException as e:
            # Handle issues with the HTTP request
            print(f"An error occured during the HTTP request: {e}")
            return {"error": "Unable to fetch product details at this time" }
        
        except KeyError as e:
            # Handle issues with the HTTP request
            print(f"Missing expected data in the response: {e}")
            return {"error": "Product detail is incomplete" }
        
        except ValueError as e:
            # Handle issues with the HTTP request
            print(f"An error occured: {e}")
            return {"error": "An unexpected error has occured" }
        
        except Exception as e:
            # Handle issues with the HTTP request
            print(f"An unexpected error has occured: {e}")
            return {"error": "An unexpected error has occured" }