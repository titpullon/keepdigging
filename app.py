# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from digging.main import MainHandler

import os
print os.path.abspath(__file__), os.getcwd()

static_path = os.path.join(os.getcwd(), "static")
print static_path


handlers = [
    (r"/", MainHandler),
    # (r"/static/(.*)", web.StaticFileHandler, {"path": "/var/www"}),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_path}),
]

params = {}

application = tornado.web.Application(handlers, **params)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()