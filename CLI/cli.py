import requests
import argparse

Base_URL="http://localhost:8000"

def add(args):
    data={
        "name":args.name,
        "category":args.category,
        "quantity":args.quantity}
    r=requests.post(
        Base_URL+"/items",
        json=data)
    print(r.json())

def list_items(args):
    r=requests.get(Base_URL+"/items")
    for item in r.json().values():
        print(item)

def delete(args):
    r=requests.delete(Base_URL+f"/items/{args.id}")
    print(r.json())

parser=argparse.ArgumentParser()
sub=parser.add_subparsers(dest="command")
add_parser=sub.add_parser("add")
add_parser.add_argument("name")
add_parser.add_argument("category")
add_parser.add_argument("quantity",type=int)
sub.add_parser("list")
delete_parser=sub.add_parser("delete")
delete_parser.add_argument("id",type=int)
args=parser.parse_args()

if args.command=="add":
    add(args)

elif args.command=="list":
    list_items(args)

elif args.command=="delete":
    delete(args)

# EL Bouns
import keyboard
import os

def add_item_cli():
    name = input("Name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))

    data = {
        "name": name,
        "category": category,
        "quantity": quantity}

    r = requests.post(Base_URL + "/items",json=data)
    print(r.json())
    input("Press Enter...")

def view_items_cli():
    r = requests.get(Base_URL + "/items")
    for item in r.json().values():
        print(item)
    input("Press Enter...")

def delete_item_cli():
    item_id = int(input("ID: "))

    r = requests.delete(Base_URL + f"/items/{item_id}")
    print(r.json())
    input("Press Enter...")

menu = ["Add Item","View Items","Delete Item","Exit"]
selected = 0

while True:
    os.system("cls")
    print("=== Inventory CLI ===\n")
    for i, item in enumerate(menu):
        if i == selected:
            print("> " + item)
        else:
            print("  " + item)
    key = keyboard.read_key()
    if key == "down":
        selected = (selected + 1) % len(menu)
    elif key == "up":
        selected = (selected - 1) % len(menu)
    elif key == "enter":

        if selected == 0:
            add_item_cli()
        elif selected == 1:
            view_items_cli()
        elif selected == 2:
            delete_item_cli()
        elif selected == 3:
            print("Bye Bye")
            break