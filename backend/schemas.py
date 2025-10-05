from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ----------------------
# Product Schemas
# ----------------------
class ProductBase(BaseModel):
    name: str
    description: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Product(ProductBase):
    id: int

# ----------------------
# Purchase Schemas
# ----------------------
class PurchaseBase(BaseModel):
    product_id: int
    quantity: int
    rate: float

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(BaseModel):
    quantity: Optional[int] = None
    rate: Optional[float] = None

class Purchase(PurchaseBase):
    id: int

# ----------------------
# Sales Schemas
# ----------------------
class SaleBase(BaseModel):
    product_id: int
    quantity: int
    rate: float

class SaleCreate(SaleBase):
    pass

class SaleUpdate(BaseModel):
    quantity: Optional[int] = None
    rate: Optional[float] = None

class Sale(SaleBase):
    id: int
