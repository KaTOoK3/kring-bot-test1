#main.py
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os 

BOT_TOKEN = os.getenv("BOT_TOKEN", "7953006027:AAHjV_dN5J9_a77bLbIdk-HTfQYrcrFDN4k")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot) 

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message): 
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Каталог",
            web_app=WebAppInfo(url="https://68171bd6f55efb05466e2b41--brilliant-buttercream-33def5.netlify.app/")
        )
    )
    await message.answer("Привет!", reply_markup=keyboard)

if __name__ == '__main__': 
    executor.start_polling(dp)