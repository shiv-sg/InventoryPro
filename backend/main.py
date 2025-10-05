from fastapi import FastAPI, HTTPException
import crud
from schemas import Product, ProductBase, Purchase, PurchaseBase, Sale, SaleBase
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

# ----------------------
# PURCHASE ROUTES
# ----------------------
# create purchase
@app.post("/purchases", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate):
    return crud.create_purchase(purchase)

# List products
@app.get("/products", response_model=List[Product])
def list_products():
    return crud.get_products()

# update purchase
@app.put("/purchases/{purchase_id}", response_model=schemas.Purchase)
def update_purchase(purchase_id: int, purchase: schemas.PurchaseUpdate):
    updated = crud.update_purchase(purchase_id, purchase)
    if not updated:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return updated

# delete purchase
@app.delete("/purchases/{purchase_id}")
def delete_purchase(purchase_id: int):
    deleted = crud.delete_purchase(purchase_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return {"message": "Purchase deleted successfully"}

# ----------------------
# SALES ROUTES
# ----------------------
# create sale
@app.post("/sales", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate):
    return crud.create_sale(sale)

# List sales
@app.get("/sales", response_model=List[Sale])
def list_sales():
    return crud.get_sales()

# update sale
@app.put("/sales/{sale_id}", response_model=schemas.Sale)
def update_sale(sale_id: int, sale: schemas.SaleUpdate):
    updated = crud.update_sale(sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated

# delete sale
@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: int):
    deleted = crud.delete_sale(sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"message": "Sale deleted successfully"}

# # Product endpoints
# # Create product
# @app.post("/products", response_model=Product)
# def create_product(product: ProductBase):
#     return crud.create_product(product)

# # List products
# @app.get("/products", response_model=List[Product])
# def list_products():
#     return crud.get_products()

# # # # Get product by name
# # # @app.get("/products/{name}", response_model=Product)
# # # def get_product_by_name(name: str):
# # #     product = crud.get_product_by_name(name)
# # #     if product is None:
# # #         raise HTTPException(status_code=404, detail="Product not found")
# # #     return product

# # # # Get product by ID
# # # @app.get("/products/{id}", response_model=Product | None)
# # # def get_product_by_id(id: int):
# # #     product = crud.get_product_by_id(id)
# # #     if product is None:
# # #         raise HTTPException(status_code=404, detail="Product not found")
# # #     return product

# # # Delete product
# # @app.delete("/products/{name}")
# # def delete_product_by_name(name: str):
# #     crud.delete_product_by_name(name)
# #     return {"message": f"Product '{name}' deleted successfully"}

# # Purchase endpoints
# # Create purchase
# @app.post("/purchases", response_model=Purchase)
# def create_purchase(purchase: PurchaseBase):
#     try:
#         return crud.create_purchase(purchase)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail="Product not found")
    
# # List purchases
# @app.get("/purchases", response_model=List[Purchase])
# def list_purchases():
#     return crud.get_purchases()

# # Sale endpoints
# # Create sale
# @app.post("/sales", response_model=Sale)
# def create_sale(sale: SaleBase):
#     try:
#         return crud.create_sale(sale)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail="Product not found")
    
# # List sales
# @app.get("/sales", response_model=List[Sale])
# def list_sales():
#     return crud.get_sales()

# Stock endpoints
# Get stock for a product
@app.get("/stock/{product_id}")
def get_stock(product_id: int):
    if not any(p.id == product_id for p in crud.products_db):
        raise HTTPException(status_code=404, detail="Product not found")
    stock = crud.get_stock_for_product(product_id)
    return {"product_id": product_id, "stock": stock}

# Get stock summary
@app.get("/stock-summary")
def get_stock_summary():
    return crud.get_stock_summary()
