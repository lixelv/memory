import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import token

bot = Bot(token)
dp = Dispatcher()

def get_command(text):
    return text.split(' ')[0].replace("/", "")

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("""Привет, отправь мне какое-нибудь\nсообщение, и я перешлю его @lixelv""")

@dp.message()
async def echo(message: types.Message):
    await bot.forward_message(1689863728, message.chat.id, message.message_id)
    await message.answer("Ваше сообщение отправлено, ожидайте ответа")
    
if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))