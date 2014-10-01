#!/usr/bin/env python

import unittest

class geovec_tests(unittest.TestCase):
    """ 
    TestCase provides multiple test assert implementations, see help(unittest.TestCase) for more details. 
    All definitions of unittest.TestCase are registered with the unittest TestRunner by default that will instantiate each derivative and sequentially call all methods found that start with 'test' 
    """
    
    def setUp(self):
        """ called before any function starting with test_ is entered """
        pass

    def tearDown(self):
        """ called after any function starting with test_ is entered """
        pass
    
    def test_module_exists(self):
        try:
            import geovec
        except:
            self.fail("geovec does not exist")
            
if __name__=="__main__":
    #instantiate and call geovec_tests
    unittest.main()
