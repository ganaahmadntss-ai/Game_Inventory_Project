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