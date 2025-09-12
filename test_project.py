import json

from project import add, update, delete, mark


with open("tasks.json", "r") as file:
    data = json.load(file)


def test_add():
    description = "Test task"
    new_task = add(data, description)

    assert new_task == {
        "id": len(data),
        "description": description,
        "status": "todo",
        "createdAt": new_task["createdAt"],
        "updatedAt": new_task["updatedAt"],
    }


def test_update():
    task_id = 2
    new_description = "Updated description"
    updated_task = update(data, task_id, new_description)

    assert updated_task["description"] == new_description
    assert updated_task["updatedAt"] == updated_task["updatedAt"]


def test_delete():
    task_id = 1
    deleted_task = delete(data, task_id)

    assert deleted_task["id"] == task_id


def test_mark():
    task_id = 1
    new_status = "completed"
    marked_task = mark(data, task_id, new_status)

    assert marked_task["status"] == new_status
    assert marked_task["updatedAt"] == marked_task["updatedAt"]
