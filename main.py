import sys
from tasks import *


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Argumento faltando")
    else:
        # arg: add
        if sys.argv[1] == "add":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                add_task(sys.argv[2])

        # arg: update
        elif sys.argv[1] == "update":
            if len(sys.argv) < 4:
                print("Argumento faltando")
            else:
                update_task(int(sys.argv[2]), sys.argv[3])

        # arg: delete
        elif sys.argv[1] == "delete":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                delete_task(int(sys.argv[2]))
    
        # arg: list
        elif sys.argv[1] == "list":
            if len(sys.argv) > 2:
                list_tasks(sys.argv[2])
            else:
                list_tasks()

        # arg: todo
        elif sys.argv[1] == "todo":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                mark_todo(int(sys.argv[2]))

        # arg: progress
        elif sys.argv[1] == "progress":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                mark_progress(int(sys.argv[2]))

        # arg: done
        elif sys.argv[1] == "done":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                mark_done(int(sys.argv[2]))

        # arg: get
        elif sys.argv[1] == "get":
            if len(sys.argv) < 3:
                print("Argumento faltando")
            else:
                get_task(int(sys.argv[2]))
        else:
            print("Digite um comando válido.")
        
