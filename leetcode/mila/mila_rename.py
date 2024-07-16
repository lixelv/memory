import re
import os
import shutil

from collections import deque


def walk(path):
    line = deque()
    line.append(path)

    while line:
        path = line.popleft()
        if os.path.isfile(path):
            if needs_handle(path):
                new_path = handle_path(path)
                shutil.move(path, new_path)
                print(f"File renamed to : {new_path}")
        else:
            for i in os.listdir(path):
                line.append(os.path.join(path, i))


def needs_handle(path) -> bool:
    return re.findall(r"\s*\((\d+)\)", path) != []


def handle_path(path):
    new_path = re.sub(r"\s*\((\d+)\)", r"_\1", path)
    return new_path


print(walk("D:\\GitHub"))
