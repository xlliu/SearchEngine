# -*- coding: utf-8 -*-
from bson import ObjectId
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class ScreenHandler(RequestAuth):

    @tornado.gen.coroutine
    def postFunc(self):
        screen = int(self.get_argument('screen'))
        taskId = ObjectId(self.get_argument('taskId'))
        data = yield self.application.getSearchResult.showResult(taskId,screen=screen)
        totalCount = yield self.application.getSearchResult.getTotalCount(taskId,screen=screen)
        if data:
            self.render('index.html', data=data, taskId=taskId, currentPage=0,pageShowNum=int(self.application.config.pageshownum), totalCounts=totalCount, screen=screen)
        else:
            self.render('index.html', data='', taskId=taskId, currentPage=0,pageShowNum=int(self.application.config.pageshownum), totalCounts=totalCount, screen=screen)