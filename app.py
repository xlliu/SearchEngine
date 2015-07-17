# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop

from basedao.gosearch import GoSearch, GetSearchResult
from basedao.gocollect import GoCollect
from basedao.gotask import GoTask
from request.collecthandler import CollectHandler
from request.pagehandler import PageHandler
from request.screenhandler import ScreenHandler
from request.screentotalnumhandler import ScreenTotalNumHandler
from request.searchhandler import SearchHomeHandler
from request.taskhandler import TaskHandler

__author__ = 'xlliu'

import tornado.web
import tornado.gen
import os


class ServerApp(tornado.web.Application):
    def __init__(self, cfg):
        self.config = cfg
        handlers = [
            (r'/',SearchHomeHandler),
            (r'/{0}'.format('index'), SearchHomeHandler),
            (r'/{0}'.format('pageHandler'), PageHandler),
            (r'/{0}'.format('screen'),ScreenHandler),
            (r'/{0}'.format('collect'),CollectHandler),
            (r'/{0}'.format('tasklist'),TaskHandler),
            (r'/{0}'.format('totalpagenum'),ScreenTotalNumHandler)
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.goSearch = GoSearch(self,
                              'searchhost',
                              'searchport',
                              'searchdbname',
                              'searchuser',
                              'searchpwd')

        self.goCollect = GoCollect(self,'searchhost',
                              'searchport',
                              'searchdbname',
                              'searchuser',
                              'searchpwd')

        self.goTask = GoTask(self,'searchhost',
                              'searchport',
                              'searchdbname',
                              'searchuser',
                              'searchpwd')

        self.getSearchResult = GetSearchResult(self,
                                               'searchresulthost',
                                               'searchresultport',
                                               'searchresultdbname',
                                               'searchresultuser',
                                               'searchresultpwd')

        IOLoop.instance().run_sync(self.init)


    @tornado.gen.coroutine
    def init(self):
        yield self.goSearch.connectionDB()
        yield self.goCollect.connectionDB()
        yield self.getSearchResult.connectionDB()
        yield self.goTask.connectionDB()