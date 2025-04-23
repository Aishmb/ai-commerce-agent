import json

def get_product_data():
    with open('app/product_data.json', 'r') as file:
        return json.load(file)
