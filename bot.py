import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils import executor

from config import TOKEN
from database.db_init import storage, run_db
from database.models import MessageInfo
from database.db_commands import set_message, get_user_messages


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет!\nЭто бот для обратной связи с подписчиками.\n\nДля связи с администратором, введите свое обращение "
        "ниже")


@dp.message_handler(content_types=ContentType.ANY)
async def send_message_to_db(message: types.Message):
    print(message)
    await set_message(message)


if __name__ == '__main__':
    print("Started")
    loop = asyncio.get_event_loop()
    loop.create_task(run_db())
    executor.start_polling(dp)
