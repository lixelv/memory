import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from cnf import token
from timeout import timeout

from programs.assembler_v1 import assembler_interpreter
from programs.binomial import expand
from programs.calculator import calc

func_dict = {
    "asm": assembler_interpreter,
    "binom": expand,
    "calc": calc
}

for i in func_dict.keys():
    func_dict[i] = timeout(12)(func_dict[i])

bot = Bot(token)
dp = Dispatcher()

def get_command(text):
    return text.split(' ')[0].replace("/", "")

def get_args(text):
    return " ".join(text.split(' ')[1:])

def format_md(text):
    text = str(text)
    for i in "+-*/^()<>`'\".:!_":
        text = text.replace(i, f"\\{i}")
    return text

@dp.message(Command(commands=['help', 'start']))
async def help(message: types.Message):
    await message.reply(f"""
/run \- основная команда в этом боте, она имеет следующий формат\:
`/\<func\> \<args\>`, пример `/binom \(\-2\.5x\+4\.3\)^6`
*\<func\>* \- отвечает за функцию, всего их {f'{len(func_dict)}  `{", ".join(func_dict.keys())}`'}\.
*\<args\>* \- отвечает за аргументы, которые передаются в функцию, например для *binom* \(раскладывает бином Ньютона\) это будет выражение вида *\(a\+b\)\^n*, где `a` \- неизвестная с множителем, `b` \- число, `n` \- степень, пример *\(\-2\.5x\+4\.3\)^6* для *asm* \(интерпретатор ассемблера\) это будет сообщение с программой на ассемблере в качестве *\<args\>* и тд\.""", parse_mode="MarkdownV2")

@dp.message(Command(commands=list(func_dict.keys())))
async def _run(message: types.Message):
    try:
        cmd = get_command(message.text)
        args = get_args(message.text)
        await message.answer("``` "+format_md(func_dict[cmd](args))+" ```", parse_mode="MarkdownV2")
    except Exception as e:
        await message.answer(f"``` {format_md(e)} ```", parse_mode="MarkdownV2")


# Настройка бота
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))
