# -*- coding: utf-8 -*-
import time
import tornado.gen

from common.requestauth import RequestAuth

__author__ = 'xlliu'


class SearchHomeHandler(RequestAuth):


    @tornado.gen.coroutine
    def postFunc(self):
        typeContent2 = self.get_argument('type2',None)
        typeContent = self.get_argument('type')
        content = self.get_argument('content')
        if typeContent2:
            taskId = yield self.application.goSearch.searchTask(typeContent, content, typeContent2=int(typeContent2))
        else:
            taskId = yield self.application.goSearch.searchTask(typeContent, content)
        data = yield self.application.goSearch.getStatusUpdate(taskId)
        totalCount = yield self.application.getSearchResult.getTotalCount(taskId)
        print 'total count', totalCount
        if data:
            self.render('index.html', data=data, taskId=taskId, currentPage=0,pageShowNum=int(self.application.config.pageshownum), totalCounts=totalCount, screen=0)
        else:
            self.render('index.html', data='', taskId=taskId, currentPage=0,pageShowNum=int(self.application.config.pageshownum), totalCounts=totalCount, screen=0)