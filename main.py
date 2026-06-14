import os
import random
import importlib.util
import sys
import utils as styling
import file_system

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

# Global variables for system state
fs = file_system.build_fs()
current_path = ["root"]
command_history = []


def main():
    styling.type_print("Booting Mini-OS Kernel...")
    styling.show_menu()

    while True:
        path_str = "/".join(current_path)
        try:
            cmd_input = input(
                f"{styling.Colors.BOLD}{path_str}> {styling.Colors.ENDC}").split()
        except EOFError:
            break

        if not cmd_input:
            continue

        cmd = cmd_input[0]
        command_history.append(" ".join(cmd_input))  # Save to history

        if cmd == "ls":
            print(list(get_current_dir().keys()))

        elif cmd == "cd":
            if len(cmd_input) > 1:
                target = cmd_input[1]
                if target == "..":
                    if len(current_path) > 1:
                        current_path.pop()
                elif target in get_current_dir():
                    current_path.append(target)
                else:
                    print(
                        f"{styling.Colors.FAIL}Directory not found!{styling.Colors.ENDC}")

        elif cmd == "tree":
            file_system.print_tree(fs)

        elif cmd == "status":
            print(f"{styling.Colors.CYAN}--- System Status ---")
            print(f"CPU Usage: {random.randint(5, 95)}%")
            print(f"Memory: {random.randint(128, 1024)} MB free")
            print(f"OS Version: Mini-OS v1.1.0{styling.Colors.ENDC}")

        elif cmd == "history":
            print(f"{styling.Colors.BLUE}Command History:{styling.Colors.ENDC}")
            for i, h in enumerate(command_history, 1):
                print(f"{i}: {h}")

        elif cmd == "run":
            if len(cmd_input) > 1:
                file_path = os.path.join(current_path[-1], cmd_input[1])
                styling.print_header(f"Executing: {cmd_input[1]}")
                try:
                    # Creating a dictionary to serve as the local/global namespace for the exec
                    # This way, 'gantt' and other variables will be accessible to the script
                    namespace = {}
                    exec(open(file_path, encoding='utf-8').read(), namespace)
                except Exception as e:
                    # Printing the error with details
                    print(
                        f"{styling.Colors.FAIL}Execution Error: {e}{styling.Colors.ENDC}")
                    import traceback
                    traceback.print_exc()  # این خط کمک می‌کند دقیقاً بفهمیم کد کجاست
            else:
                print("Usage: run [filename.py]")

# Helper for main.py navigation


def get_current_dir():
    d = fs
    for p in current_path:
        d = d[p]
    return d


if __name__ == "__main__":
    main()
