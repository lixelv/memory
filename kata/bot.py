from aiogram import Bot, Dispatcher, types, executor
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
#####

bot = Bot(token)
dp = Dispatcher(bot)

def format_md(text):
    text = str(text)
    for i in "+-*/^()<>`'\".:!_":
        text = text.replace(i, f"\\{i}")
    return text

@dp.message_handler(commands=['help', 'start'])
async def help(message: types.Message):
    await message.reply(f"""
/run \- основная команда в этом боте, она имеет следующий формат\:
`/\<func\> \<args\>`, пример `/binom \(\-2\.5x\+4\.3\)^6`
*\<func\>* \- отвечает за функцию, всего их {f'{len(func_dict)}  `{", ".join(func_dict.keys())}`'}\.
*\<args\>* \- отвечает за аргументы, которые передаются в функцию, например для *binom* \(раскладывает бином Ньютона\) это будет выражение вида *\(a\+b\)\^n*, где `a` \- неизвестная с множителем, `b` \- число, `n` \- степень, пример *\(\-2\.5x\+4\.3\)^6* для *asm* \(интерпретатор ассемблера\) это будет сообщение с программой на ассемблере в качестве *\<args\>* и тд\.""", parse_mode=types.ParseMode.MARKDOWN_V2)

@dp.message_handler(commands=list(func_dict.keys()))
async def run(message: types.Message):
    cmd = message.get_command().replace("/", "")
    args = message.get_args()
    
    await message.answer("```"+format_md(func_dict[cmd](args))+"```", parse_mode=types.ParseMode.MARKDOWN_V2)



# Run the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)