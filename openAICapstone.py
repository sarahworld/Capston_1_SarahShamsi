from openai import OpenAI
import os
from models import Questions
import json

from dotenv import load_dotenv
load_dotenv()

class OpenAICapstone:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def call(self, product_name):
        _questions = {"origin_country": f"What is the country of origin of {product_name}?  Give one word answer.",
                      "is_vegetarian": f"Is {product_name} vegetarian or not? give one word boolean answer as True or False",
                      "confidence_percentage": f"What is your confidence percentage of {product_name} being vegetarian? Give one word answer."}
        # question = f"What is the country of origin of {product_name}? Is it vegetarian or not give boolean answer? What is your confidence percentage of it being vegetarian? Give answer as a json with the keys origin_country, is_vegetarian and confidence_percentage. The answer should be only word for each."
        # completion = self.client.chat.completions.create(
        # model="gpt-3.5-turbo",
        # messages=[
        #     {"role": "user", "content": question}]
        # )
        # print(f"question: {question}")
        # content = completion.choices[0].message.content
        # content = json.loads(content)
        # print("Insideeee",content)
        # print(type(content))
        
        result = {}
        for key, _q in _questions.items():
            completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": _q}]
            )
            content = completion.choices[0].message.content
            result[key] = content

        print(f"FINAL - {result}")    
        #content =['Ethiopia','Yes','95%']
        # 060383041168
      
        # return  Questions.serialize_product_questions(content)
        # return content
        return result
    
    