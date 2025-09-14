import argparse
import json
from datetime import datetime
from tabulate import tabulate  # type: ignore
import pyttsx3  # type: ignore


def main():
    # Handle command-line arguments
    parser = argparse.ArgumentParser(description="Task Management CLI")
    parser.add_argument("-a", help="Add new task", type=str)
    parser.add_argument("-u", help="Update existing task", nargs=2)
    parser.add_argument("-d", help="Delete task", type=int)
    parser.add_argument("-mc", help="Mark task as completed", type=int)
    parser.add_argument("-mi", help="Mark task as in-progress", type=int)
    parser.add_argument("-l", help="List all tasks", action="store_true")
    parser.add_argument("-lc", help="List completed tasks", action="store_true")
    parser.add_argument("-li", help="List in-progress tasks", action="store_true")
    args = parser.parse_args()

    # Read the current tasks
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Apply the requested operation and save changes
    def handle_add():
        result = add(data, args.a)
        confirm(f"Task {result['id']} added successfully.")

    def handle_update():
        result = update(data, *args.u)
        if result:
            confirm(f"Task {result['id']} updated successfully.")
        else:
            confirm("Task not found.")

    def handle_delete():
        result = delete(data, args.d)
        if result:
            confirm(f"Task {result['id']} deleted successfully.")
        else:
            confirm("Task not found.")

    def handle_mark_completed():
        result = mark(data, args.mc, "completed")
        if result:
            confirm(f"Task {result['id']} marked as completed.")
        else:
            confirm("Task not found.")

    def handle_mark_in_progress():
        result = mark(data, args.mi, "in-progress")
        if result:
            confirm(f"Task {result['id']} marked as in-progress.")
        else:
            confirm("Task not found.")

    # Action dispatch table
    actions = [
        (args.a, handle_add),
        (args.u, handle_update),
        (args.d, handle_delete),
        (args.mc, handle_mark_completed),
        (args.mi, handle_mark_in_progress),
        (args.l, lambda: list_tasks(data)),
        (args.lc, lambda: list_tasks(data, "completed")),
        (args.li, lambda: list_tasks(data, "in-progress")),
    ]

    # Execute the first matching action
    for condition, action in actions:
        if condition:
            action()
            return

    # Show help if no action was taken
    parser.print_help()


def add(data: list, description: str) -> dict:
    # Find the highest existing ID and increment by 1
    max_id = 0
    if data:
        max_id = max(task["id"] for task in data)

    # Create the new task
    new_task = {
        "id": max_id + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().date().isoformat(),
        "updatedAt": datetime.now().date().isoformat(),
    }
    data.append(new_task)

    # Save the updated data back to the file
    save(data)

    return new_task


def update(data: list, *args) -> dict:
    # Find and update the task
    for task in data:
        if task["id"] == int(args[0]):
            task["description"] = args[1]
            task["updatedAt"] = datetime.now().date().isoformat()
            break

    # Save the updated data back to the file
    save(data)

    return task


def delete(data: list, task_id: int) -> dict | None:
    task_to_delete = None
    for task in data:
        if task["id"] == task_id:
            task_to_delete = task
            break

    # Remove the task if found
    if task_to_delete:
        data.remove(task_to_delete)

    # Reassign IDs to maintain sequential order
    for i, task in enumerate(data, 1):
        task["id"] = i

    # Save the updated data back to the file
    save(data)

    return task_to_delete


def mark(data: list, task_id: int, status: str) -> dict:
    # Find and update the task status
    for task in data:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().date().isoformat()
            break

    # Save the updated data back to the file
    save(data)

    return task


def save(data: list) -> None:
    # Save the updated data back to the file
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


def list_tasks(data: list, status: str | None = None) -> None:
    # Filter tasks by status if provided
    if status:
        filtered_data = [task for task in data if task["status"] == status]
        if not filtered_data:
            print(f"No {status} tasks found.")
            return
    else:
        filtered_data = data
        if not filtered_data:
            print("No tasks found.")
            return

    # Prepare table data
    headers = ["ID", "Description", "Status", "Created At", "Updated At"]
    table = [
        [
            task["id"],
            task["description"],
            task["status"],
            task["createdAt"],
            task["updatedAt"],
        ]
        for task in filtered_data
    ]

    # Print the table using tabulate
    print(tabulate(table, headers, tablefmt="grid"))


def confirm(pharse: str) -> None:
    # Initialize engine for text-to-speech feature
    engine = pyttsx3.init()
    print(pharse)
    engine.say(pharse)
    engine.runAndWait()


if __name__ == "__main__":
    main()
