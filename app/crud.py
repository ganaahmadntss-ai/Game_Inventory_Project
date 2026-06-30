from app.supabase_client import supabase

def create_item(item):
    data = {"name": item.name,"category": item.category,"quantity": item.quantity}
    response = supabase.table("items").insert(data).execute()
    return response.data

def get_items():
    response = (supabase.table("items").select("*").execute())
    return response.data

def get_item(item_id):
    response = (supabase.table("items").select("*").eq("id", item_id).execute())
    return response.data

def delete_item(id):
    response = supabase.table("items").delete().eq("id", id).execute()
    if not response.data:
        return {"message": "Item not found"}
    return response.data