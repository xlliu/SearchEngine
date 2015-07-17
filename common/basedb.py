# -*- coding: utf-8 -*-
import motor
import tornado.gen

__author__ = 'xlliu'


class BaseDB(object):
    def __init__(self,app):
        self.app = app



class BaseDBHandler(BaseDB):
    def __init__(self,app,host,port,dbName,user,pwd):
        BaseDB.__init__(self,app)
        self._db = None
        self._mc = None

        self.host = host
        self.port = port
        self.dbName = dbName
        self.user = user
        self.pwd = pwd

    @tornado.gen.coroutine
    def connectionDB(self):
        self._mc = motor.MotorClient(getattr(self.app.config,self.host), int(getattr(self.app.config,self.port)))
        self._db = self._mc[getattr(self.app.config,self.dbName)]

        ret = yield self._db.authenticate(getattr(self.app.config,self.user), getattr(self.app.config, self.pwd))
        print '安全认证成功'
        if not ret:
            raise Exception('Authenticate Error')

