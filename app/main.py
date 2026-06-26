from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate
from app import model

app = FastAPI(title="Game Inventory API",version="1.0.0")

@app.post("/items")
def add_item(item:ItemCreate):
    return model.create_item(item.dict())

@app.get("/items")
def get_all():
    return model.get_items()

@app.get("/items/{item_id}")
def get_one(item_id:int):
    items=model.get_items()
    if item_id not in items:
        raise HTTPException(404,"Item not found")

    return items[item_id]

@app.delete("/items/{item_id}")
def delete(item_id:int):
    deleted=model.delete_item(item_id)
    if not deleted:
        raise HTTPException(404,"Item not found")
        
    return {"message":"deleted"}