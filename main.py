
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, WebAppInfo
from aiogram import types
from aiogram_dialog import (
    Dialog, DialogManager, setup_dialogs, StartMode, Window,
)
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

import handlers


class MySG(StatesGroup):
    main = State()


main_window = Window(
    Const("Hello, unknown person"),
    Button(Const("open web"), id="nothing", web_app=WebAppInfo(url="https://github.com/SwEEtL0Li/test/blob/master/test.html")),
    state=MySG.main,
)
dialog = Dialog(main_window)

storage = MemoryStorage()
bot = Bot(token='6525353343:AAHW8JVm3wya_x52NdUXM5lAuBqZX-afgL8')
dp = Dispatcher(storage=storage)
dp.include_router(dialog)
setup_dialogs(dp)



@dp.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)