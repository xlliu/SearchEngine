# -*- coding: utf-8 -*-
from common.basedb import BaseDBHandler
import tornado.gen
__author__ = 'xlliu'

class GoTask(BaseDBHandler):

    @tornado.gen.coroutine
    def showTask(self,sortType='create_time',var=-1,sc='a',currentPage = 0):
        data = None
        if sc=='a':
            data = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':100004},{'job_list.type':100003},
                                                                             {'job_list.type':10002},{'job_list.type':5}]},
                                                                     {'name':1,'status':1,'comment':1,
                                                                      'current_progress':1,'create_time':1,
                                                                      'complete_time':1},
                                                                     limit=int(self.app.config.taskshownum),
                                                                     skip=currentPage*int(self.app.config.taskshownum)).sort(sortType,var).to_list(None)
        if sc=='s':
            data = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':10002},{'job_list.type':5}]},
                                                                     {'name':1,'status':1,'comment':1,
                                                                      'current_progress':1,'create_time':1,
                                                                      'complete_time':1},
                                                                     limit=int(self.app.config.taskshownum),
                                                                     skip=currentPage*int(self.app.config.taskshownum)).sort(sortType,var).to_list(None)
        if sc=='c':
            data = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':100004},{'job_list.type':100003}]},
                                                                     {'name':1,'status':1,'comment':1,
                                                                      'current_progress':1,'create_time':1,
                                                                      'complete_time':1},
                                                                     limit=int(self.app.config.taskshownum),
                                                                     skip=currentPage*int(self.app.config.taskshownum)).sort(sortType,var).to_list(None)
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def getTotalCount(self,sc):
        total = None
        if sc == 'a':
            total = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':100004},{'job_list.type':100003},
                                                                             {'job_list.type':10002},{'job_list.type':5}]},
                                                                     ).count()
        if sc == 's':
            total = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':10002},{'job_list.type':5}]},
                                                                     ).count()

        if sc == 'c':
            total = yield self._db[self.app.config.searchcollection].find({'$or':[{'job_list.type':100004},{'job_list.type':100003}]},
                                                                     ).count()
        raise tornado.gen.Return(total)