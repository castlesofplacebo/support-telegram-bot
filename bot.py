import asyncio
import json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils import executor

from config import TOKEN
from database.db_init import storage, run_db
from database.models import MessageInfo

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


@dp.message_handler(commands=['search'])
async def search_by_username(message: types.Message):
    argument = message.get_args()
    message_list = await MessageInfo.filter(username=argument).values("data")
    for i in message_list:
        # to chat
        str_message = i.get('data')
        dict_message = json.loads(str_message)
        new_msg = types.Message(**dict_message)
        await new_msg.send_copy(message.chat.id)

        # to console
        # print(i.get('data'))


@dp.message_handler(content_types=ContentType.ANY)
async def send_message(message: types.Message):
    await MessageInfo(username=message.from_user.id, data=str(message)).save()
    await message.reply("Ваше сообщение отправлено администратору")


if __name__ == '__main__':
    print("Started")
    loop = asyncio.get_event_loop()
    loop.create_task(run_db())
    executor.start_polling(dp)
