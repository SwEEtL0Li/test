
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import WebAppInfo

bot = Bot(token='6525353343:AAHW8JVm3wya_x52NdUXM5lAuBqZX-afgL8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Web App', web_app=WebAppInfo(url="https://2ch.hk/")))
    await message.reply("Hello!", reply_markup=markup)

executor.start_polling(dp)
