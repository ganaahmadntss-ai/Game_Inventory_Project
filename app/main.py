from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate
from app import model


app = FastAPI(title="Game Inventory API", version="1.0.0")

@app.post("/items")
def add_item(item: ItemCreate):
    return model.create_item(item.model_dump())

@app.get("/items")
def get_all():
    return model.get_items()

@app.get("/items/{item_id}")
def get_one(item_id: int):
    items = model.get_items()
    if isinstance(items, list):
        for item in items:
            if item["id"] == item_id:
                return item

    elif item_id in items:
        return items[item_id]

    raise HTTPException(status_code=404,detail="Item not found")

@app.delete("/items/{item_id}")
def delete(item_id: int):
    deleted = model.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Item not found")

    return {"message": "deleted"}