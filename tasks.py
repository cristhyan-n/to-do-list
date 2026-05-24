from datetime import datetime
from storage import load_tasks, save_tasks

def add_task(description):
    load = load_tasks()
    if not load:
        id = 1
    else:
    # ver sobre a parte da lista dentro de max para entender melhor o que acontece ali
        id = max([task["id"] for task in load]) + 1
    tasks_list = {
        "id": id, "description": description, "status": "todo", "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()
    }
    load.append(tasks_list)
    save_tasks(load)
    print(f"Tarefa {id}-{description} adicionada com sucesso.")

def find_task(load, id):
    for task in load:
        if task["id"] == id: 
            return task
    return None

def get_task(id):
    load = load_tasks()
    task = find_task(load, id)
    if task:
        print(f"ID: {task['id']} | {task['description']} | {task['status']} | {task['createdAt']}")
    else:
         print("ID não encontrado")


def update_task(id, description):
    load = load_tasks()
    task = find_task(load, id)
    if task:
        task["description"] = description
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(load)
        print(f"Tarefa {id}-{description} atualizada com sucesso.")
    else:
        print(f"ID não encontrado")

def delete_task(id):
    load = load_tasks()
    task = find_task(load, id)
    if task:
        description = task["description"]
        load.remove(task)
        save_tasks(load)
        print(f"Tarefa {id}-{description} removida com sucesso.")
    else:
        print(f"ID não encontrado")

def list_tasks(filter=None):
    load = load_tasks()
    if len(load) == 0:
        print("Lista vazia")
    else:
        if filter == None:
            for task in load:
                print(f"ID: {task['id']} | {task['description']} | {task['status']} | {task['createdAt']}")
        else:
            if filter == "delete":
                    save_tasks([])
                    print("Lista apagada com sucesso.")
            else:
                for task in load:
                        if task["status"] == filter:
                            print(f"ID: {task['id']} | {task['description']} | {task['status']} | {task['createdAt']}")

def mark_status(id, status):
    load = load_tasks()
    task = find_task(load, id)
    if task:
        task["status"] = status
        task["updatedAt"] = datetime.now().isoformat()
        save_tasks(load)
        print(f"Status da tarefa {id}-{task['description']} atualizada para {status} com sucesso.")
    else:
        print(f"ID não encontrado")

def mark_done(id):
        mark_status(id, "done")

def mark_progress(id):
        mark_status(id, "progress")

def mark_todo(id):
        mark_status(id, "todo")
