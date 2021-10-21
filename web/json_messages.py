import json
from database.db_commands import get_all_messages, get_user_messages


def to_json(message_list):
    json_list = []
    for i in message_list:
        str_message = i.get('data')
        json_list.append(json.loads(str_message))
    return json_list


async def json_all_messages():
    message_list = await get_all_messages()
    return to_json(message_list)


async def json_user_messages(user_id):
    message_list = await get_user_messages(user_id)
    return to_json(message_list)
