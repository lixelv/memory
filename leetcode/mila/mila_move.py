import os
import re
import shutil
import traceback

from collections import deque


def walk(path: str, save_path: str):
    line = deque()
    line.append(path)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    while line:
        path = line.popleft()

        if os.path.isfile(path):
            try:
                handle(path, save_path)
            except Exception as e:
                tb = traceback.extract_tb(e.__traceback__)[-1]
                print(f"{path} - {e}\nline: {tb.lineno} - {tb.filename}")
                print(f"Алярм бебе ошибочкаааааа!")
        else:
            for i in os.listdir(path):
                line.append(os.path.join(path, i))


def handle(path: str, save_path: str):  # НФ-00000550-1123194 (не найдено)_done.png
    if "_done" not in path or path[-4:] not in [".jpg", ".png"]:
        return

    name, extension = get_name_extension(path)

    name = name.lower()
    name = name.replace("_done", "")

    if "(не найдено)" not in name:
        name = re.sub(r"\(.+\)", "", name)

    name = name.strip()

    if "(не найдено)" in name or "-" not in name:
        index = name.replace("(не найдено)", "")
        brand = "different"
    else:
        splited = name.split("-")

        index = "-".join(splited[:-1])
        brand = splited[-1]

    brand = brand.replace(" ", "")
    name = index + extension

    save_folder = os.path.join(save_path, brand)
    save_file = os.path.join(save_folder, name)

    i = 1
    while os.path.exists(save_file):
        name = index + f" ({i})" + extension
        save_file = os.path.join(save_folder, name)
        i += 1

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    shutil.move(path, save_file)


def get_name_extension(path: str):
    full_name = re.findall(r"[^\\/]+$", path)[0]

    name = (
        re.findall(r"(.+)\..*$", full_name)
        or re.findall(r"(.+)\.?.*$", full_name)
        or [""]
    )[0]
    extension = (re.findall(r"\..+$", full_name) or [""])[0]

    return name, extension


print(
    walk(
        "D:\\GitHub\\memory\\leetcode\\mila\\images",
        "D:\\GitHub\\memory\\leetcode\\mila\\save",
    )
)
