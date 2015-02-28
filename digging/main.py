# -*- coding: utf-8 -*-

from tornado import template
from tornado.web import RequestHandler


class MainHandler(RequestHandler):

    def get(self):
        params = {"p1": "param1", "qwerty": "ssddwe"}
        self.render("base.html", params=params)


class AboutHandler(RequestHandler):

    def get(self):
        self.render("about.html")


class PostsHandler(RequestHandler):

    def get(self):
        posts = [{"title": "post 1",
                  "date": "updated 12.04.2015",
                  "body": "normal text <strong>bold one</strong>",
                  "tags": ["post", "norm"]},
                 {"title": "post 2",
                  "date": "updated 05.12.2015",
                  "body": "normal text <b>bold one</b>",
                  "tags": ["python", "tornado"]}]
        self.render("posts.html", posts=posts)