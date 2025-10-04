from typing import List
from pydantic import BaseModel

# Product schema
class Product(BaseModel):
    id: int
    name: str # Product name
    description: str # Product description
    purchase_price: float # Product price
    quantity: int # Available quantity
    selling_price: float # Selling price

# In-memory database
products_db: List[Product] = []

# CRUD Operations
def create_product(product: Product) -> Product:
    products_db.append(product)
    return product

def get_products() -> List[Product]:
    return products_db

def get_product_by_name(name: str) -> Product | None:
    for product in products_db:
        if product.name == name:
            return product
    return None

def get_product_by_id(id:int) -> Product | None:
    for product in products_db:
        if product.id == id:
            return product
    return None

def delete_product_by_id(id: int) -> bool:
    global products_db
    products_db = [product for product in products_db if product.id != id]
    return True

def delete_product_by_name(name: str) -> bool:
    global products_db
    products_db = [product for product in products_db if product.name != name]
    return True