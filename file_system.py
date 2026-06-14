import os


def build_fs():
    fs = {"root": {}}
    for folder in os.listdir("."):
        if os.path.isdir(folder) and folder not in [".git", "__pycache__", ".vscode"]:
            fs["root"][folder] = {}
            for file in os.listdir(folder):
                fs["root"][folder][file] = "file"
    return fs


def print_tree(d, level=0):
    for key, value in d.items():
        print("  " * level + f"|-- {key}")
        if isinstance(value, dict):
            print_tree(value, level + 1)
