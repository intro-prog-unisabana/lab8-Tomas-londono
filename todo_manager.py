"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    """Reads tasks from a file. Returns a list of tasks."""
    # TODO: Implementar manejo de FileNotFoundError según README.md
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []

    raise NotImplementedError


def write_todo_file(file_path, tasks):
    """Writes tasks to a file, one per line."""
    # TODO: Implementar escritura de tareas según README.md
    try:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    raise NotImplementedError
