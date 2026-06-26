from fastapi import FastAPI, HTTPException
from schemas import ItemCreate
import model

app = FastAPI(title="Game Inventory API",version="1.0.0")

@app.post("/items")
def add_item(item:ItemCreate):
    return models.create_item(item.dict())

@app.get("/items")
def get_all():
    return models.get_items()

@app.get("/items/{item_id}")
def get_one(item_id:int):
    items=models.get_items()
    if item_id not in items:
        raise HTTPException(404,"Item not found")

    return items[item_id]

@app.delete("/items/{item_id}")
def delete(item_id:int):
    deleted=models.delete_item(item_id)
    if not deleted:
        raise HTTPException(404,"Item not found")

    return {"message":"deleted"}