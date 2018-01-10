#coding=utf-8

import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from utils.utils import sendMail


def createHTML():
    u'''创建可以运行所有脚本的discover'''
    start_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(start_dir, 
                                                   pattern = 'test_*.py', 
                                                   top_level_dir = None)
    #创建html报告
    
    nowTime = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
    fileName = './report/'+nowTime+'_result.html'
    stream = open(fileName,'wb')
    
    runner = HTMLTestRunner(stream = stream,
                         title = u"care业务系统自动化测试报告",
                         description = u"用例执行情况",
                         verbosity = 2)
    
        
    runner.run(discover)
        
    stream.close()
    
if __name__ == "__main__" :
    createHTML()
#     sendMail()