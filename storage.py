import os, json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError("Arquivo Corrompido") from e

    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)