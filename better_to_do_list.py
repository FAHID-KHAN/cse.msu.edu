from typing import List,Dict,Optional

def print_menu() -> None :
    print("To do cli")
    print("1) Add menu ")
    print("2) List Task")
    print("3) Mark Done")
    print("4) Delete Task")
    print("5) Exit")


def get_choice() -> int:
    while True:
        choice = input("Choose (1-5): ").strip()
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= 5:
                return n
        print("Invalid choice.Enter a number from 1 to 5")


def next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(int(t["id"]) for t in tasks) + 1

def add_task(tasks: List[Task]) -> None:
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty")
        return 

    tasks.append({"id": next_id(tasks),"title":title,"done": False})
    print("Added.")
