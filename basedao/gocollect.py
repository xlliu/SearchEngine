# -*- coding: utf-8 -*-
from datetime import datetime
from bson import ObjectId
from common.basedb import BaseDBHandler

import tornado.gen
__author__ = 'xlliu'

class GoCollect(BaseDBHandler):

    """
    job_group_id:{api:1,www:0}
    """
    @tornado.gen.coroutine
    def collectTask(self,tdId,collectType,titleName,ty):
        collect_id = yield self._db[self.app.config.searchcollection].insert({
            'type': 1,
            'name': 'CT%s%s' % (collectType,datetime.now().strftime('%Y%m%d')),
            'create_time': None,
            'complete_time': None,
            'current_progress': 0,
            'status': 0,
            'job_group_id': ObjectId('556fc51d5f08330c7e70238e') if 1 == int(ty) else ObjectId('556fc5545f08330c7e70238f'),
            'owner': ObjectId('5551c1a118f0648d34e40479'),
            'account_fbid':None,
            'job_list' : [
            {
                "group_id" : int(tdId),
                "type" : int(collectType),
            }],
            'comment' : titleName
        })
        print "%s  collect"%collect_id
        raise tornado.gen.Return(collect_id)