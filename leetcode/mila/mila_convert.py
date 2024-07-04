import os
from rembg import remove
from PIL import Image
import rawpy


def process_image(input_path: str, output_path: str) -> None:
    """
    Убирает фон из изображения и сохраняет его по указанному пути.

    Parameters:
    input_path (str): Полный путь к исходному файлу изображения.
    output_path (str): Полный путь для сохранения обработанного изображения.
    """
    try:
        # Открываем изображение в зависимости от формата
        if input_path.lower().endswith(".cr2"):
            with rawpy.imread(input_path) as raw:
                img = Image.fromarray(raw.postprocess())
        else:
            img = Image.open(input_path)

        result = remove(img)

        # Конвертируем изображение в PNG перед сохранением
        result = result.convert("RGBA")
        output_path = os.path.splitext(output_path)[0] + ".png"
        result.save(output_path)
        print(f"Done: {input_path} to {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


def process_folder(folder_path: str) -> None:
    """
    Убирает фон из изображений в указанной папке и сохраняет их по указанному пути.

    Parameters:
    folder_path (str): Полный путь к папке с изображениями.
    """
    items = os.listdir(folder_path)

    for image_file in items:
        extension = image_file.split(".")[-1].lower()
        name = ".".join(image_file.split(".")[:-1])

        if extension not in ["jpg", "jpeg", "png", "cr2"]:
            continue

        input_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(folder_path, name + "_done." + extension)
        process_image(input_path, output_path)

    print(f"Done: {folder_path}")


def process_folder_of_folders(folder_path: str) -> None:
    if not os.path.isdir(folder_path):
        print(f"The path {folder_path} is not a valid directory.")
        return

    folders = [
        os.path.join(folder_path, i)
        for i in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, i))
    ]

    for folder in folders:
        process_folder(folder)

    print("All DONE!")


if __name__ == "__main__":
    input_path = input("Enter the path to the folder containing subfolders: ").strip()
    process_folder_of_folders(input_path)
