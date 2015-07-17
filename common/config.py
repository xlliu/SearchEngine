# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
from threading import Thread
import time


__author__ = 'xlliu'
class Config(object):


    def __init__(self,configFile,section):
        self.configFile = configFile
        self.section = section
        self.cp = ConfigParser()
        self.readConfigFile()

    def readOption(self):
        self.cp.read(self.configFile)
        return self.cp.options(self.section)

    def getOptionValue(self,option):
        try:
            return self.cp.get(self.section,option)
        except:
            return None

    def readConfigFile(self):
        for option in self.readOption():
            setattr(self, option, self.getOptionValue(option))



class WhileReadConfigFile(Thread):

    def __init__(self,whileMethod,whileTime = 5):
        super(WhileReadConfigFile,self).__init__()
        self.setDaemon(True)
        self.whileMethod = whileMethod
        self.whileTime = whileTime

    def run(self):
        while True:
            time.sleep(self.whileTime)
            self.whileMethod.readConfigFile()