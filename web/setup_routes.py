from web.views import index

def setup_routes(app):
    app.router.add_get('/', index)
    # app.router.add_get('/all', index)
    # app.router.add_get('/chat/{id}', index)
    # app.router.add_post('/sendMessage', send)