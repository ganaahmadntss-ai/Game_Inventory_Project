from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate
from app import schemas, crud

app = FastAPI(title="Game Inventory API", version="1.0.0")

@app.post("/items")
def add_item(item: schemas.ItemCreate):
    return crud.create_item(item)

@app.get("/items")
def get_all():
    return crud.get_items()

@app.get("/items/{item_id}")
def get_one(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    return item[0]

@app.delete("/items/{item_id}")
def delete(item_id: int):
    deleted = crud.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"message": "deleted"}