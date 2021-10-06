from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType
from tortoise import Tortoise, fields, run_async

from config import TOKEN
from database.db_init import storage, run_db
from database.models import MessageInfo

import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет!\nЭто бот для обратной связи с подписчиками.\n\nДля связи с администратором, введите свое обращение "
        "ниже")


@dp.message_handler(commands=['get'])
async def get_messages(message: types.Message):
    print(await MessageInfo.all().values())


@dp.message_handler(content_types=ContentType.ANY)
async def send_message(message: types.Message):
    await MessageInfo(data=str(message)).save()
    await message.reply("Ваше сообщение отправлено администратору")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(run_db())
    executor.start_polling(dp)
