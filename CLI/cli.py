import argparse
import readchar
import os
from commands import (
    add,
    list_items,
    delete,
    add_item_cli,
    view_items_cli,
    delete_item_cli)

def menu_loop():
    menu = ["Add Item","View Items","Delete Item","Exit"]
    selected = 0

    while True:
        os.system("clear" if os.name == "posix" else "cls")
        for i,item in enumerate(menu):
            if i == selected:
                print("> " + item)
            else:
                print("  " + item)
        key = readchar.readkey()

        if key == readchar.key.DOWN:
            selected = (selected + 1) % len(menu)

        elif key == readchar.key.UP:
            selected = (selected - 1) % len(menu)

        elif key == readchar.key.ENTER:
            if selected == 0:
                add_item_cli()
            elif selected == 1:
                view_items_cli()
            elif selected == 2:
                delete_item_cli()
            elif selected == 3:
                break


parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")
add_parser = sub.add_parser("add")
add_parser.add_argument("name")
add_parser.add_argument("category")
add_parser.add_argument("quantity", type=int)
sub.add_parser("list")

delete_parser = sub.add_parser("delete")
delete_parser.add_argument("id", type=int)
args = parser.parse_args()


if args.command == "add":
    add(args)
elif args.command == "list":
    list_items(args)
elif args.command == "delete":
    delete(args)
else:
    menu_loop()