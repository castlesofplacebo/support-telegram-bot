from aiogram import types
from database.models import MessageInfo


async def set_message(message: types.Message):
    return await MessageInfo(username=message.from_user.id, data=str(message)).save()


async def get_all_messages():
    return await MessageInfo.all().values("data")


async def get_user_messages(user_id):
    return await MessageInfo.filter(username=user_id).values("data")
