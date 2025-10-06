from typing import List
from datetime import datetime
from backend import schemas

# In-memory databases
products_db: List[schemas.Product] = []
purchases_db: List[schemas.Purchase] = []
sales_db: List[schemas.Sale] = []

product_id_counter = 1
purchase_id_counter = 1
sale_id_counter = 1


# ----------------------
# PRODUCT CRUD
# ----------------------
def create_product(product: schemas.ProductCreate):
    global product_id_counter
    new_product = schemas.Product(id=product_id_counter, **product.dict())
    products_db.append(new_product)
    product_id_counter += 1
    return new_product

def get_products():
    return products_db

def update_product(product_id: int, product_update: schemas.ProductUpdate):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            updated_data = product.dict()
            update_fields = product_update.dict(exclude_unset=True)
            updated_data.update(update_fields)
            products_db[index] = schemas.Product(**updated_data)
            return products_db[index]
    return None

def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product.id == product_id:
            return products_db.pop(index)
    return None


# # Product CRUD
# def create_product(product: schemas.ProductBase) -> schemas.Product:
#     global product_id_counter
#     new_product = schemas.Product(id=product_id_counter, **product.dict())
#     products_db.append(new_product)
#     product_id_counter += 1
#     return new_product


# def get_products() -> List[schemas.Product]:
#     return products_db


# ----------------------
# PURCHASE CRUD
# ----------------------
def create_purchase(purchase: schemas.PurchaseCreate):
    global purchase_id_counter
    # validate product exists
    if not any(p.id == purchase.product_id for p in products_db):
        raise ValueError("Product not found")
    new_purchase = schemas.Purchase(id=purchase_id_counter, **purchase.dict())
    purchases_db.append(new_purchase)
    purchase_id_counter += 1
    return new_purchase


def get_purchases():
    return purchases_db


def update_purchase(purchase_id: int, purchase_update: schemas.PurchaseUpdate):
    for index, purchase in enumerate(purchases_db):
        if purchase.id == purchase_id:
            updated_data = purchase.dict()
            update_fields = purchase_update.dict(exclude_unset=True)
            updated_data.update(update_fields)
            purchases_db[index] = schemas.Purchase(**updated_data)
            return purchases_db[index]
    return None


def delete_purchase(purchase_id: int):
    for index, purchase in enumerate(purchases_db):
        if purchase.id == purchase_id:
            return purchases_db.pop(index)
    return None


# Purchase CRUD
def create_purchase(purchase: schemas.PurchaseBase) -> schemas.Purchase:
    global purchase_id_counter
    # validate product exists
    if not any(p.id == purchase.product_id for p in products_db):
        raise ValueError("Product does not exist")
    new_purchase = schemas.Purchase(id=purchase_id_counter, date=datetime.now(), **purchase.dict())
    purchases_db.append(new_purchase)
    purchase_id_counter += 1
    return new_purchase


def get_purchases() -> List[schemas.Purchase]:
    return purchases_db

# ----------------------
# SALES CRUD
# ----------------------
def create_sale(sale: schemas.SaleCreate):
    global sale_id_counter
    # validate product exists
    if not any(p.id == sale.product_id for p in products_db):
        raise ValueError("Product not found")
    new_sale = schemas.Sale(id=sale_id_counter, **sale.dict())
    sales_db.append(new_sale)
    sale_id_counter += 1
    return new_sale


def update_sale(sale_id: int, sale_update: schemas.SaleUpdate):
    for index, sale in enumerate(sales_db):
        if sale.id == sale_id:
            updated_data = sale.dict()
            update_fields = sale_update.dict(exclude_unset=True)
            updated_data.update(update_fields)
            sales_db[index] = schemas.Sale(**updated_data)
            return sales_db[index]
    return None


def delete_sale(sale_id: int):
    for index, sale in enumerate(sales_db):
        if sale.id == sale_id:
            return sales_db.pop(index)
    return None


# Sale CRUD
def create_sale(sale: schemas.SaleBase) -> schemas.Sale:
    global sale_id_counter
    # validate product exists
    if not any(p.id == sale.product_id for p in products_db):
        raise ValueError("Product does not exist")
    new_sale = schemas.Sale(id=sale_id_counter, date=datetime.now(), **sale.dict())
    sales_db.append(new_sale)
    sale_id_counter += 1
    return new_sale


def get_sales() -> List[schemas.Sale]:
    return sales_db


# Stock calculation
def get_stock_for_product(product_id: int) -> int:
    total_purchased = sum(p.quantity for p in purchases_db if p.product_id == product_id)
    total_sold = sum(s.quantity for s in sales_db if s.product_id == product_id)
    return total_purchased - total_sold


def get_all_stocks() -> List[dict]:
    stocks = []
    for product in products_db:
        stock = get_stock_for_product(product.id)
        stocks.append({"product_id": product.id, "name": product.name, "stock": stock})
    return stocks


def get_stock_summary():
    summary = []

    for product in products_db:
        total_purchased = sum(
            p.quantity for p in purchases_db if p.product_id == product.id
        )
        total_sold = sum(
            s.quantity for s in sales_db if s.product_id == product.id
        )
        current_stock = total_purchased - total_sold

        summary.append({
            "product_id": product.id,
            "product_name": product.name,
            "total_purchased": total_purchased,
            "total_sold": total_sold,
            "current_stock": current_stock
        })

    return summary





# # Product schema
# class Product(BaseModel):
#     id: int
#     name: str # Product name
#     description: str # Product description
#     purchase_price: float # Product price
#     quantity: int # Available quantity
#     selling_price: float # Selling price

# # In-memory database
# products_db: List[Product] = []

# # CRUD Operations
# def create_product(product: Product) -> Product:
#     products_db.append(product)
#     return product

# def get_products() -> List[Product]:
#     return products_db

# def get_product_by_name(name: str) -> Product | None:
#     for product in products_db:
#         if product.name == name:
#             return product
#     return None

# def get_product_by_id(id:int) -> Product | None:
#     for product in products_db:
#         if product.id == id:
#             return product
#     return None

# def delete_product_by_id(id: int) -> bool:
#     global products_db
#     products_db = [product for product in products_db if product.id != id]
#     return True

# def delete_product_by_name(name: str) -> bool:
#     global products_db
#     products_db = [product for product in products_db if product.name != name]
#     return True