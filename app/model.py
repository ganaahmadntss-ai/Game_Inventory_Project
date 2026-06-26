from database import Inventory

def create_item(item):
    global counter
    Inventory[counter] = item
    Inventory[counter]["id"] = counter
    counter += 1
    return Inventory[counter-1]

def get_items():
    return Inventory

def delete_item(item_id):
    if item_id not in Inventory:
        return False
    del Inventory[item_id]
    return True