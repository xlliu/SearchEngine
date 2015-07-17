# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth

import tornado.gen
__author__ = 'xlliu'


class CollectHandler(RequestAuth):

    @tornado.gen.coroutine
    def postFunc(self):
        tdId = self.get_argument('tdId')
        collectType = self.get_argument('collectType')
        titleName = self.get_argument('titleName')
        ty = self.get_argument('ty')
        collect_id = yield self.application.goCollect.collectTask(tdId=tdId,collectType=collectType,titleName=titleName,ty=ty)
        if collect_id:
            self.write('1')