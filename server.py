# -*- coding: utf-8 -*-

from aiohttp import web

async def get_handler(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def post_handler(request):
    data = await request.json()
    print(data)
    return web.Response(text='request')

async def put_handler(request):
    pass    

app = web.Application()
app.add_routes([web.get('/getmethod', get_handler),
                web.get('/getmethod/{name}', get_handler),
                web.post('/post', post_handler),
                web.put('/put', put_handler)])

web.run_app(app)