# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
from bson.json_util import dumps

__author__ = 'xlliu'


class TaskHandler(RequestAuth):


    @tornado.gen.coroutine
    def getFunc(self):
        totalCount = yield self.application.goTask.getTotalCount(sc='a')
        lastPage = (int(totalCount)+int(self.application.config.taskshownum)-1)/int(self.application.config.taskshownum)-1
        self.render('tasklist.html',currentPage=0,lastPage=lastPage,sc="a")

    @tornado.gen.coroutine
    def postFunc(self):
        typeContent = self.get_argument('typeContent',None)
        var = self.get_argument('b',None)
        sc = self.get_argument('sc','a')
        currentPage = int(self.get_argument('currentPage',0))
        if typeContent:
            data = yield self.application.goTask.showTask(sortType=typeContent,var=int(var),sc=sc,currentPage=currentPage)
        else:
            data = yield self.application.goTask.showTask(sc=sc,currentPage=currentPage)
        self.write(dumps(data))