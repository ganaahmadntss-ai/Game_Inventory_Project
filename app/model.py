from app.database import Inventory

def create_item(item):
    item_id = len(Inventory) + 1
    Inventory[item_id] = item
    Inventory[item_id]["id"] = item_id
    return Inventory[item_id]


def get_items():
    return Inventory

def delete_item(item_id):
    if item_id not in Inventory:
        return False
    del Inventory[item_id]
    return True