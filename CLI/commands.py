import requests
BASE_URL = "https://gameinventoryproject-production.up.railway.app"
def add(args):
    data = {
        "name": args.name,
        "category": args.category,
        "quantity": args.quantity}

    r = requests.post(BASE_URL + "/items", json=data)
    r.raise_for_status()
    print(r.json())

def list_items(args):
    r = requests.get(BASE_URL + "/items")
    r.raise_for_status()
    items = r.json()

    for item in items if isinstance(items, list) else items.values():
        print(item)

def delete(args):
    r = requests.delete(BASE_URL + f"/items/{args.id}")
    r.raise_for_status()
    print(r.json())

def add_item_cli():
    name = input("Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))

    data = {
        "name": name,
        "category": category,
        "quantity": quantity}

    r = requests.post(BASE_URL + "/items", json=data)
    r.raise_for_status()
    print(r.json())
    input("Press Enter...")

def view_items_cli():
    r = requests.get(BASE_URL + "/items")
    r.raise_for_status()
    items = r.json()

    for item in items if isinstance(items, list) else items.values():
        print(item)
    input("Press Enter...")

def delete_item_cli():
    item_id = int(input("ID: "))
    r = requests.delete(BASE_URL + f"/items/{item_id}")
    r.raise_for_status()
    print(r.json())
    input("Press Enter...")