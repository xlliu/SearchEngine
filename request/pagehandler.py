# -*- coding: utf-8 -*-
from bson import ObjectId
from bson.json_util import dumps
from common.requestauth import RequestAuth

import tornado.gen
__author__ = 'xlliu'

class PageHandler(RequestAuth):

    @tornado.gen.coroutine
    def postFunc(self):
        screen = int(self.get_argument('screen'))
        taskId = ObjectId(self.get_argument('taskId'))
        currentPage = int(self.get_argument('currentPage'))
        data = yield self.application.getSearchResult.showResult(taskId,currentpage=currentPage,screen=screen)
        self.write(dumps(data))