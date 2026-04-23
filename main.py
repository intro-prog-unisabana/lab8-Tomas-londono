"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file


def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"
  remove "task"
  view
""")
            return

        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)

        i = 2
        write_needed = False

        while i < len(sys.argv):
            cmd = sys.argv[i]

            if cmd == "view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                i += 1

            elif cmd == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                task = sys.argv[i + 1]
                tasks.append(task)
                print(f'Task "{task}" added.')
                write_needed = True
                i += 2

            elif cmd == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')
                task = sys.argv[i + 1]
                try:
                    tasks.remove(task)
                    print(f'Task "{task}" removed.')
                    write_needed = True
                except ValueError:
                    print(f'Task "{task}" not found.')
                i += 2

            else:
                raise ValueError("Command not found!")

        if write_needed:
            write_todo_file(file_path, tasks)

    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print(f"File {sys.argv[1]} not found! Returning an empty to-do list.")


if __name__ == "__main__":
    main()
# TODO: Implementar CLI según README.md
