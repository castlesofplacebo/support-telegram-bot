import webbrowser
import json
import aiofiles

from database.db_commands import get_all_messages


async def json_messages():
    message_list = await get_all_messages()
    json_list = []
    for i in message_list:
        str_message = i.get('data')
        dict_message = json.loads(str_message)
        json_list.append(dict_message)
    return json_list


async def user_messages(user_id):
    message_list = await get_all_messages()
    json_list = []
    for i in message_list:
        json_message = json.loads(i.get('data'))
        json_id = json_message['from']['id']
        if json_id == user_id:
            json_list.append(json_message)
    return json_list


async def get_html(user_id):
    async with aiofiles.open(f'messages.html', mode='w') as f:
        await f.write(
            f"""<html>
                    <head>
                    <title>CodeX support bot</title>
                    </head>
                    <body>
                        <header>
                            <h3>All messages:</h3>
                        </header>
                        <main>
                            <p>{await user_messages(user_id)}</p>
                        </main>
                        <footer></footer>
                    </body>
                </html>""")
        webbrowser.open('messages.html')
