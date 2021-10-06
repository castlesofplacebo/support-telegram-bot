from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет!\nЭто бот для обратной связи с подписчиками.\n\nДля связи с администратором, введите свое обращение "
        "ниже")


@dp.message_handler(content_types=ContentType.ANY)
async def send_message(msg: types.Message):
    # TODO save in db
    await msg.reply("Ваше сообщение отправлено администратору")


if __name__ == '__main__':
    executor.start_polling(dp)
