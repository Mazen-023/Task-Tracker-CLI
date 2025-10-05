# Task Tracker CLI
#### Video Demo:  <URL [HERE](https://youtu.be/8bB_1TBx-0A)>
#### Repo URL:  <URL [HERE](https://roadmap.sh/projects/task-tracker)>

## Description:

A command-line interface (CLI) tool for managing tasks and to-do lists. The task manager support CRUD operations for tasks with different status levels.

## Task Properties

Each task has the following properties:

* `id`: A unique identifier for the task
* `description`: A short description of the task
* `status`: The status of the task (todo, in-progress, done)
* `createdAt`: The date and time when the task was created
* `updatedAt`: The date and time when the task was last updated

## Project Structure

### project.py

The main application file containing all core functionality:

* __Command-line argument parsing__ using Python's `argparse` module for intuitive user interaction
* __Task operations__ including add, update, delete, and mark status functions
* __Data persistence__ through JSON file management with proper error handling
* __Clean architecture__ using a dispatch table pattern for command execution
* __Type safety__ with full `mypy` compliance using modern Python type hints

### tasks.json

The data storage file that persists all task information:

* Stores tasks as a `JSON` array with structured task dictionaries
* Automatically created when first task is added
* Maintains data integrity across program sessions

### test_project.py 

Comprehensive test suite ensuring code reliability:

* Unit tests for all major functions using `pytest` framework

### requirements.txt

Project dependencies specification includes:

* `tabulate` for beautiful table formatting
* `pytest` for testing
* `pyttsx3` for text-to-speech functionality

## Project Functionalities

__main()__

The entry point of the application. It handles command-line argument parsing using `argparse`, loads existing tasks from the JSON file (or creates an empty list if the file doesn't exist).

__add(data, description)__

```
"""
Creates a new task with the provided description and adds it to the task list.

:param data: The list of tasks where we will add new task
:type data: list
:param description: The description for the new task
:type description: str
:return: The newly created task dictionary
:rtype: dict
"""
```

__update(data, *args)__

```
"""
Modifies the description of an existing task identified by its ID.

:param data: The list of existing tasks
:type data: list
:param task_id: The ID of the task to update (from args tuple)
:type task_id: str
:param new_description: The new description for the task (from args tuple)
:type new_description: str
:return: The updated task dictionary
:rtype: dict
"""
```

__delete(data, task_id)__

```
"""
Removes a task from the list and implements ID resequencing.

:param data: The list of existing tasks
:type data: list
:param task_id: The ID of the task to delete
:type task_id: int
:return: The deleted task dictionary or None if task not found
:rtype: dict | None
"""
```

__mark(data, task_id, status)__

```
"""
Changes the status of a specified task to "completed" or "in-progress".

:param data: The list of existing tasks
:type data: list
:param task_id: The ID of the task to mark
:type task_id: int
:param status: The new status for the task
:type status: str
:return: The updated task dictionary
:rtype: dict
"""
```

__save(data)__

```
"""
Handles file I/O operations for persisting task data to JSON file.

:param data: The task data to save to file
:type data: list
:return: None
:rtype: None
"""
```

__list_tasks(data, status=None)__

```
"""
Displays tasks in a formatted table using the tabulate library.

:param data: The list of tasks to display
:type data: list
:param status: Optional status filter ("completed", "in-progress")
:type status: str | None
:return: None (prints to console)
:rtype: None
"""
```

__confirm(pharse)__

```
"""
Speaks a given phrase aloud using text-to-speech and prints it to the console.

:param pharse: The phrase to be spoken and printed
:type pharse: str
:return: None
:rtype: None
"""
```

## Helper Functions in Main

The main function also contains several inline helper functions that encapsulate the logic for different operations:

* `handle_add()` Wraps the add function and provides user feedback with success messages.

* `handle_update()` Wraps the update function and displays confirmation of the update operation.

* `handle_delete()` Wraps the delete function and handles both successful deletions and cases where the specified task doesn't exist.

* `handle_mark_completed()` & `handle_mark_in_progress()` Wrap the mark function for specific status changes and provide appropriate user feedback.

## Key Features

### Task Operations
* __Add tasks__ (`-a`) with automatic unique ID
* __Update task__ (`-u`) with timestamp tracking
* __Delete tasks__ (`-d`) with automatic ID
* __Status management__ with separate commands for marking tasks as completed (`-mc`) or in-progress (`-mi`)

### Listing and Filtering
* __List all tasks__ (`-l`) in a formatted table view
* __Filter by status__ with dedicated commands for completed (`-lc`) and in-progress (`-li`) tasks

## Usage Examples

```bash
# Add a new task
python project.py -a "CS50 Python final project"

# List all tasks
python project.py -l

# Mark task as completed
python project.py -mc 1

# Update task description
python project.py -u 1 "Submit CS50 Python final project"

# List only completed tasks
python project.py -lc

# Delete a task
python project.py -d 1
```
