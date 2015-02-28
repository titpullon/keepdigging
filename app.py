# -*- coding: utf-8 -*-

import os
import tornado.ioloop
from tornado.web import url, StaticFileHandler, Application

from digging.main import MainHandler, PostsHandler, AboutHandler


static_path = os.path.join(os.getcwd(), "static")


handlers = [
    url(r"/static/(.*)", StaticFileHandler, {"path": static_path}),
    url(r"/", MainHandler),
    url(r"/posts", PostsHandler, name="posts"),
    url(r"/about", AboutHandler, name="about"),
]


params = {"template_path": "templates",
          "debug": True}


application = Application(handlers, **params)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()