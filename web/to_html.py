import webbrowser
import json
import aiofiles

from database.models import MessageInfo


async def json_messages():
    message_list = await MessageInfo.all().values("data")
    json_list = []
    for i in message_list:
        str_message = i.get('data')
        dict_message = json.loads(str_message)
        json_list.append(dict_message)
    return json_list


async def get_html():
    async with aiofiles.open(f'messages.html', mode='w') as f:
        # TODO: обращение к ассинхронным функциям внутри get_html()
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
                            <p>{str(await MessageInfo.all().values("data"))}</p>
                        </main>
                        <footer></footer>
                    </body>
                </html>""")
        webbrowser.open('messages.html')
