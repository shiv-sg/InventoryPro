from fastapi import FastAPI
import crud
from crud import Product
from typing import List

# Initialize FastAPI app
app = FastAPI(title="InventoryPro API", version="1.0.0")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to InventoryPro API"}

# Test endpoint
@app.get("/test")
def read_test():
    return {"message": "This is a test endpoint"}

# Status endpoint
@app.get("/status")
def status():
    return {
        "status": "API is running smoothly",
        "app": "InventoryPro API",
        "version": "1.0.0"
        }
    
# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API is healthy"}

# Product endpoints
# Create product
@app.post("/product", response_model=Product)
def create_product(product: Product):
    return crud.create_product(product)

# List products
@app.get("/products", response_model=List[Product])
def list_products():
    return crud.get_products()

# Get product by name
@app.get("/products/{name}", response_model=Product)
def get_product_by_name(name: str):
    product = crud.get_product_by_name(name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Get product by ID
@app.get("/products/{id}", response_model=Product | None)
def get_product_by_id(id: int):
    product = crud.get_product_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Delete product
@app.delete("/products/{name}")
def delete_product_by_name(name: str):
    crud.delete_product_by_name(name)
    return {"message": f"Product '{name}' deleted successfully"}
