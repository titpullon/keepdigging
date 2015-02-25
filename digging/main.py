# -*- coding: utf-8 -*-

import tornado.web
from tornado import template


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        params = {"p1": "param1", "qwerty": "ssddwe"}
        loader = template.Loader("templates")
        data = loader.load("base.html").generate(params=params)
        self.write(data)
        # self.write("Hello, world")
