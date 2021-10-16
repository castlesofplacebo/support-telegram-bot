import asyncio

from aiohttp import web
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType

from config import TOKEN
from database.db_init import storage, run_db
from database.models import MessageInfo
from database.db_commands import set_message
from web.setup_routes import setup_routes

app = web.Application()
setup_routes(app)
loop = asyncio.get_event_loop()
bot = Bot(TOKEN, loop=loop)
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


async def on_startup(app):
    await run_db()
    asyncio.create_task(dp.start_polling())


async def on_shutdown(app):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    print("Started")

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app)
