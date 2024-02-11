import re

cmd_pattern = r'^[a-zA-Z]+'
args_pattern = r"('[^']*'|\w+)"

line = "mov, a, 'b, v', c"  # Пример строки

parsed_line = re.findall("('[^']*'|\w+)", line)
cmd = parsed_line[0]
args = parsed_line[1:] if len(parsed_line) > 1 else []

print(f"Команда: {cmd}, Аргументы: {args}")