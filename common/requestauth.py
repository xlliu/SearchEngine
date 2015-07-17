# -*- coding: utf-8 -*-
__author__ = 'xlliu'

import tornado.web
import tornado.gen


class RequestAuth(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        yield self.getFunc()

    @tornado.gen.coroutine
    def post(self):
        yield self.postFunc()

    @tornado.gen.coroutine
    def getFunc(self):
        self.render("indexdoor.html",
                    data='',
                    taskId='',
                    currentPage=0,
                    pageShowNum=int(self.application.config.pageshownum),
                    totalCounts=0,
                    screen=0)

    @tornado.gen.coroutine
    def postFunc(self):
        pass