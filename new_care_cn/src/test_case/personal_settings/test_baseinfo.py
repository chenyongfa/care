import time
import unittest

from contant.contant import Contant


class B(unittest.TestCase):
    def test_b(self):
        print Contant.userName
        print 'test baseinfo'
        print 'test baseinfo'
        print 'test baseinfo'
        print 'test baseinfo'
 
        print 'test baseinfo'
        self.assertTrue(True)
        
    def runTest(self):
        pass
