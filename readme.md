# Game Inventory Project 
A simple game inventory management system built with FastAPI and a CLI client.
# Run Backend
uvicorn app.main:app --reload

## Endpoints
GET /items
GET /items/{id}
POST /items
PUT /items/{id}
DELETE /items/{id}


## CLI
Add:
python cli/cli.py add name category quantity

List:
python cli/cli.py list

Delete:
python cli/cli.py delete id

## Features
- FastAPI Backend
- REST API
- Pydantic Data Validation
- CRUD Operations (Create, Read, Update, Delete)
- Database Integration
- CLI Client
- Swagger API Documentation


## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
# 2. Open project folder
cd Game_Inventory_Project

# 3. Install dependencies
pip install -r requirements.txt

---
    # Run Backend
#Start the FastAPI server:
uvicorn app.main:app --reload

# The server will run on:
http://127.0.0.1:8000

# API documentation:
http://127.0.0.1:8000/docs


---

# CLI Usage
The CLI client allows you to manage your inventory from the terminal.

# Add Item
python cli/cli.py add "Item Name" "Category" Quantity

# Example:
python cli/cli.py add "Sword" "Weapon" 10
---

# List Items
python cli/cli.py list

---

# Delete Item
python cli/cli.py delete ITEM_ID

# Example:
python cli/cli.py delete 1

---

# Project Structure

Game_Inventory_Project/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│
├── cli/
│   └── cli.py
│
├── requirements.txt
└── README.md


---

# Technologies Used
Python
FastAPI
Pydantic
SQLAlchemy
Requests

---
# Cross Platform
The CLI application works on Windows and macOS.