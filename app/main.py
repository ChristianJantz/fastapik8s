from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List

items = [
    {"name": "Computer", "preis": 1000.00, "type": "Hardware"},
    {"name": "Monitor", "preis": 200.00, "type": "Hardware"},
    {"name": "Windows", "preis": 300.00, "type": "Software"}
]

class ItemTypeEnum(Enum):
    HARDWARE = "Hardware"
    SOFTWARE = "Software"

class ItemModel(BaseModel):
    name: str
    price: float = Field(100.00, gt= 0, lt=9999.99)
    type: ItemTypeEnum
    
class ResponseItem(BaseModel):
    name: str
    type: ItemTypeEnum
    

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello from fastapi World"}

@app.get("/items")
async def get_items():
    return items

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str=None):
#     return {"item_id": item_id, "q": q}