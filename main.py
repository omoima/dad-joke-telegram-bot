from aiogram import *
from dad_functions import dad_message, dad_text
import os

default = "Type 'hello' to receive a dad joke"
bot = Bot(token=os.getenv('dadjokebot'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Send a message when the command /start is issued."""
    await message.reply(default)

@dp.message_handler()
async def dadjoke(message: types.Message):
    """Send the dad joke."""
    print("HERE")
    if dad_message(message.text):
        await message.reply(dad_text())
    else:
        await message.reply(default)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)