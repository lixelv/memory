import re

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r"(Example)", "### Example", text)
text = re.sub(r"(Input:|Output:|Explanation:)\s*([^\n]+)", r"- \1 `\2`", text)

with open("input.txt", "w", encoding="utf-8") as f:
    f.write(text)
