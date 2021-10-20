from web.views import index, get_all, get_chat, send


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/all', get_all)
    app.router.add_get('/chat', get_chat)  # request "/chat?user_id=..."
    app.router.add_post('/send', send)
