# -*- coding: utf-8 -*-

from tornado import template
from tornado.web import RequestHandler
from tornado.gen import coroutine


class MainHandler(RequestHandler):

    def get(self):
        params = {"p1": "param1", "qwerty": "ssddwe"}
        self.render("base.html", params=params)


class AboutHandler(RequestHandler):

    @coroutine
    def get(self):
        db = self.settings["db"]
        author = yield db.author_data.find_one()

        self.render("about.html", author=author)


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