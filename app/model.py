from app.supabase_client import supabase

def create_item(item):
    data = item.model_dump()
    response = supabase.table("items").insert(data).execute()
    return response.data[0] if response.data else None

def get_items():
    response = supabase.table("items").select("*").execute()
    return response.data

def get_item(item_id):
    response = (supabase.table("items").select("*").eq("id", item_id).single().execute())
    return response.data if response.data else None

def delete_item(item_id):
    response = (supabase.table("items").delete().eq("id", item_id).execute())
    return len(response.data) > 0