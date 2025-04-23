from fastapi import APIRouter
from pydantic import BaseModel
import json
import os
from app import qa, recommend, image_search

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    description: str
    image_url: str

def get_product_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "product_data.json")
    with open(json_path, "r") as f:
        return json.load(f)

@router.get("/recommendations", response_model=list[Product])
async def recommend_products(query: str):
    products = get_product_data()
    recommended_products = [
        product for product in products if query.lower() in product['description'].lower()
    ]
    return [Product(**prod) for prod in recommended_products]
