# -*- coding: utf-8 -*-

import os
import tornado.ioloop
from tornado.web import url, StaticFileHandler, Application
from motor import MotorClient

from digging.main import MainHandler, PostsHandler, AboutHandler


static_path = os.path.join(os.getcwd(), "static")


handlers = [
    url(r"/static/(.*)", StaticFileHandler, {"path": static_path}),
    url(r"/", MainHandler),
    url(r"/posts", PostsHandler, name="posts"),
    url(r"/about", AboutHandler, name="about"),
]


db = MotorClient("localhost", 27017).keepdigging_db

params = {"template_path": "templates",
          "db": db,
          "debug": True}


application = Application(handlers, **params)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()