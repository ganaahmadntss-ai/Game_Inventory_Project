from app.database import Inventory

def create_item(item):
    if Inventory:
        item_id = max(Inventory.keys()) + 1
    else:
        item_id = 1

    item["id"] = item_id
    Inventory[item_id] = item
    return item

def get_items():
    return Inventory

def get_item(item_id):
    return Inventory.get(item_id)

def delete_item(item_id):
    if item_id not in Inventory:
        return False

    del Inventory[item_id]
    return True