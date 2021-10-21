import asyncio

from aiohttp import web
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType

from config import TOKEN
from database.db_init import storage, run_db
from database.models import MessageInfo
from database.db_commands import set_message
from web.json_messages import json_all_messages, json_user_messages


async def send(request):
    post = await request.post()
    chat_id = post.get('chat_id')
    message = post.get('message')

    await send_message_to_chat(chat_id, message)
    return web.Response(text='message sent to chat')


async def index(request):
    return web.Response(text='Hey there!')


async def get_all(request):
    return web.json_response(await json_all_messages())


async def get_chat(request):
    params = request.rel_url.query
    user_id = params['user_id']
    return web.json_response(await json_user_messages(user_id))


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/all', get_all)
    app.router.add_get('/chat', get_chat)  # request "/chat?user_id=..."
    app.router.add_post('/send', send)


async def send_message_to_chat(chat_id, message):
    await send_message_to_db(await bot.send_message(chat_id, message))


async def on_startup(app):
    await run_db()
    asyncio.create_task(dp.start_polling())


async def on_shutdown(app):
    await dp.storage.close()
    await dp.storage.wait_closed()


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
    await set_message(message)


if __name__ == '__main__':
    print("Started")

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app)
