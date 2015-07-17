# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class ScreenTotalNumHandler(RequestAuth):

    @tornado.gen.coroutine
    def postFunc(self):
        screen = self.get_argument('sc','a')
        totalCount = yield self.application.goTask.getTotalCount(sc=screen)
        lastPage = (int(totalCount)+int(self.application.config.taskshownum)-1)/int(self.application.config.taskshownum)-1
        self.write(str(lastPage))