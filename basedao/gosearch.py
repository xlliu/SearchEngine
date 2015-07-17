# -*- coding: utf-8 -*-
from datetime import datetime
import time
from bson import ObjectId

import tornado.gen

from common.basedb import BaseDBHandler


__author__ = 'xlliu'


class GoSearch(BaseDBHandler):
    @tornado.gen.coroutine
    def searchTask(self, typeContent, content, typeContent2 = 10002):
        taskId = yield self._db[self.app.config.searchcollection].insert({
            'type': 1,
            'name': 'ST%s%s%s' %(typeContent2,datetime.now().strftime('%Y%m%d'),content if len(content)<5 else content[4]),
            'create_time': None,
            'complete_time': None,
            'current_progress': 0,
            'status': 0,
            'job_group_id':ObjectId('556fc2bb5f08330c7e702375'),
            'owner':ObjectId('5551c1a118f0648d34e40479'),
            'account_fbid':None,
            'job_list' : [
            {
              "type" : typeContent2,
              'search_type':int(typeContent),
              'search_word':content,
              'search_max_num':20,
            }]
        })
        print "%s  search"%taskId
        raise tornado.gen.Return(taskId)

    @tornado.gen.coroutine
    def getStatusUpdate(self, taskId):
        i = 0
        while True:
            status = yield self._db[self.app.config.searchcollection].find_one({'_id': taskId,
                                                                                'status':2},{'_id': 1})
            i += 1
            print 'status:%s,已查询数据库%s次等待查询结果中...' %(status,i)
            if status:
                print '查到结果准备输出'
                data = yield self.app.getSearchResult.showResult(taskId)
                raise tornado.gen.Return(data)
            if i==int(self.app.config.searchtimeout):
                raise Exception('Search Timeout')
            time.sleep(1)

class GetSearchResult(BaseDBHandler):


    @tornado.gen.coroutine
    def showResult(self, taskId, currentpage = 0,screen = 0):
        data = None
        if screen == 0:
            data = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId},
                                                                                           {'head_url': 1, 'title': 1,
                                                                                            'type': 1, 'visit_url': 1,
                                                                                            'description':1,'fbid' : 1},
                                                                                           limit=int(self.app.config.pageshownum),
                                                                                           skip=currentpage * int(self.app.config.pageshownum)
                        ).to_list(None)
        if screen == 1:
            data = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'User'},
                                                                                           {'head_url': 1, 'title': 1,
                                                                                            'type': 1, 'visit_url': 1,
                                                                                            'description':1,'fbid' : 1},
                                                                                           limit=int(self.app.config.pageshownum),
                                                                                           skip=currentpage * int(self.app.config.pageshownum)
                        ).to_list(None)
        if screen == 2:
            data = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Group'},
                                                                                           {'head_url': 1, 'title': 1,
                                                                                            'type': 1, 'visit_url': 1,
                                                                                            'description':1,'fbid' : 1},
                                                                                           limit=int(self.app.config.pageshownum),
                                                                                           skip=currentpage * int(self.app.config.pageshownum)
                        ).to_list(None)
        if screen == 3:
            data = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Page'},
                                                                                           {'head_url': 1, 'title': 1,
                                                                                            'type': 1, 'visit_url': 1,
                                                                                            'description':1,'fbid' : 1},
                                                                                           limit=int(self.app.config.pageshownum),
                                                                                           skip=currentpage * int(self.app.config.pageshownum)
                        ).to_list(None)
        if screen == 4:
            data = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Event'},
                                                                                           {'head_url': 1, 'title': 1,
                                                                                            'type': 1, 'visit_url': 1,
                                                                                            'description':1,'fbid' : 1},
                                                                                           limit=int(self.app.config.pageshownum),
                                                                                           skip=currentpage * int(self.app.config.pageshownum)
                        ).to_list(None)
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def getTotalCount(self,taskId,screen=0):
        totalCounts = None
        if screen == 0:
            totalCounts = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId}).count()
        if screen == 1:
            totalCounts = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'User'}).count()
        if screen == 2:
            totalCounts = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Group'}).count()
        if screen == 3:
            totalCounts = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Page'}).count()
        if screen == 4:
            totalCounts = yield self._db[self.app.config.searchresultcollection].find({'job_id': taskId,'type':'Event'}).count()
        raise tornado.gen.Return(totalCounts)