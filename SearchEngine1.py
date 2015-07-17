#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import ServerApp
from common.config import Config
from common.config import WhileReadConfigFile

CONFIG_FILE = 'db.cfg'
APP_CONFIG_SECTION = 'dbMeg'

def run():

    onLoadConfig = Config(CONFIG_FILE,APP_CONFIG_SECTION)
    WhileReadConfigFile(onLoadConfig).start()

    http_server = HTTPServer(ServerApp(onLoadConfig))
    http_server.listen(8090)
    IOLoop.instance().start()

if __name__ == '__main__':
    run()