# Task Manager Project 

## Description
A simple REST API project using FastAPI and CLI.
The system allows users to create,
view and delete tasks.



## Run Backend
Install requirements:
pip install -r requirements.txt
Start server:
uvicorn backend.main:app --reload

## CLI Commands
Add Task:
python cli/cli.py add "Study Python"


List Tasks:
python cli/cli.py list

Delete Task:
python cli/cli.py delete 1


## Features
- FastAPI Backend
- Pydantic Validation
- REST API
- CLI Client