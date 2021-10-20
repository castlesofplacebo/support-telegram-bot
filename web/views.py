from aiohttp import web
from web.json_messages import json_all_messages, json_user_messages
from database.models import MessageInfo
from aiogram import types


async def index(request):
    return web.Response(text='Hey there!')


async def get_all(request):
    return web.json_response(await json_all_messages())


async def get_chat(request):
    params = request.rel_url.query
    user_id = params['user_id']
    return web.json_response(await json_user_messages(user_id))


async def send(request):
    post = await request.post()
    chat_id = post.get('chat_id')
    message = post.get('message')
    print(chat_id, ' ', message)
    # sending to telegram
    # add to db as tg-message
    return web.Response(text='ok')
