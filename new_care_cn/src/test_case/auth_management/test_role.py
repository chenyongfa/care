#coding=utf-8

import time 
import unittest

from contant.contant import Contant


class A(unittest.TestCase):
    u'''权限管理角色用例'''
    def test_a(self):
        u''''删除角色用例'''
        print Contant.userName
        print 'test role'
        print 'test role'
        print 'test role'
        print 'test role'
 
        print 'test role'
        self.assertTrue(True)
        
    def runTest(self):
        pass


if __name__ == "__main__":
    B = A()
    B.test_a()