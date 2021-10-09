import webbrowser


async def test_html():
    f = open('messages.html', 'w')

    html_template = """<html>
    <head>
    <title>All messages</title>
    </head>
    <body>
    <h2>Welcome</h2>

    <p>Messages goes here...</p>

    </body>
    </html>
    """

    f.write(html_template)
    f.close()

    webbrowser.open('messages.html')
