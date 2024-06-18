from aiogram import types
from aiogram_dialog import DialogManager
from aiogram.types import WebAppInfo

async def start_page(callback_query: types.CallbackQuery, dialog_manager: DialogManager):
    await callback_query.message.answer("Opening web app...",
                                        reply_markup=types.InlineKeyboardMarkup().add(
                                            types.InlineKeyboardButton(text='Open Web App',
                                                                       web_app=types.WebAppInfo(url='https://github.com/oooazimut/GigaBot'))
                                        ))