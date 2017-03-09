'''
Created on 6 Mar 2017

@author: pigna
'''
import unittest
from main import Stack


class Test(unittest.TestCase):


    def testAdd(self):
        s = Stack()
        s.add("1")
        s.add("2")
        self.assertTrue(s.size() == 2)
    
    def testRemove(self):
        s = Stack()
        s.add("1")
        s.add("2")
        s.remove()
        self.assertTrue(s.size() == 1) 
    
    def testSize(self):
        s = Stack()
        s.add("1")
        self.assertTrue(s.size() == 1) 
        s.remove()
        self.assertFalse(s.size() == 1)
    
    def testEmpty(self):
        s=Stack()
        self.assertTrue(s.isEmpty())
        s.add("Stuff")
        self.assertFalse(s.isEmpty())
    
    def testLastelement(self):
        s=Stack()
        s.add("Andy")
        self.assertTrue(s.check_last_item()=="Andy")
        s.add("Pignanelli")
        self.assertTrue(s.check_last_item()=="Pignanelli")

    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAdd']
    unittest.main()