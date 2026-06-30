from fastapi import FastAPI, HTTPException
from app.supabase_client import supabase
from app.schemas import ItemCreate, ItemUpdate

app = FastAPI(title="Game Inventory API",version="1.0.0")

@app.get("/items")
def get_items():
    result = (supabase.table("items").select("*").execute())
    return result.data

@app.get("/items/{item_id}")
def get_item(item_id:int):
    result = (supabase.table("items").select("*").eq("id", item_id).execute())

    if not result.data:
        raise HTTPException(404,"Item not found")
    return result.data[0]

@app.post("/items")
def create_item(item:ItemCreate):
    result = (supabase.table("items").insert(item.model_dump()).execute())
    return result.data[0]

@app.put("/items/{item_id}")
def update_item(
    item_id:int,
    item:ItemUpdate):
    data = {
        k:v
        for k,v in item.model_dump().items()
        if v is not None}
    result = (supabase.table("items").update(data).eq("id", item_id).execute())

    if not result.data:
        raise HTTPException(404,"Item not found")
    return result.data[0]

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    result = (supabase.table("items").delete().eq("id", item_id).execute())

    if not result.data:
        raise HTTPException(404,"Item not found")
    return {"message":"Deleted successfully"}