'''
Created on Apr 1, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Queue as qu
import CA05.prod.Word as wd

class Test(unittest.TestCase):
    def testInitExists(self):
        q = qu.Queue()
        assert "__init__" in dir(q), 'Method by name __init__ does not exists'
    
    def testIsEmptyExists(self):
        q = qu.Queue()
        assert "isEmpty" in dir(q), 'Method by name isEmpty does not exists'
        
    def testEnqueueExists(self):
        q = qu.Queue()
        assert "enqueue" in dir(q), 'Method by name enqueue does not exists'
        
    def testDequeueExists(self):
        q = qu.Queue()
        assert "dequeue" in dir(q), 'Method by name dequeue does not exists'
        
    def testSizeExists(self):
        q = qu.Queue()
        assert "size" in dir(q), 'Method by name size does not exists'
        
    def testQInstantiation(self):
        q = qu.Queue()
        assert isinstance(q, qu.Queue), 'queue is not an instance of Queue'

    def testEmptyQIsEmpty(self):
        q = qu.Queue()
        self.assertEqual(q.isEmpty(), True , 'isEmpty does not work properly')
     
    def testNonEmptyQIsEmpty(self):
        q = qu.Queue()
        w = wd.Word(address = 22)
        q.enqueue(word = w)
        self.assertEqual(q.isEmpty(), False , 'isEmpty does not work properly')
        
    def testEnqueueIntoEmptyQ(self):
        q = qu.Queue()
        w = wd.Word(address = 22)
        q.enqueue(word = w)
        self.assertEqual(q.size(), 1 , 'Enqueue does not work properly')
        
    def testEnqueueIntoNonEmptyQ(self):
        q = qu.Queue()
        w1 = wd.Word(address = 22)
        w2 = wd.Word(address = 3)
        q.enqueue(word = w1)
        q.enqueue(word = w2)
        self.assertEqual(q.size(), 2 , 'Enqueue does not work properly')
              
    def testDequeueFromEmptyQErrorType(self):
        q = qu.Queue()
        self.assertRaises(ValueError, q.dequeue)
        
    def testDequeueFromEmptyQErrorMessage(self):
        q = qu.Queue()
        self.assertRaisesRegexp(Exception, "^Queue.dequeue:\s\s", q.dequeue)
    
    def testDequeueFromNonEmptyQReturnValue(self):
        q = qu.Queue()
        w1 = wd.Word(address = 22)
        w2 = wd.Word(address = 3)
        q.enqueue(word = w1)
        q.enqueue(word = w2)
        self.assertEqual(q.dequeue().getTerminalAddress(), 22 , 'Dequeue does not work properly')
        
    def testDequeueFromNonEmptyQQueueStatus(self):
        q = qu.Queue()
        w1 = wd.Word(address = 22)
        w2 = wd.Word(address = 3)
        q.enqueue(word = w1)
        q.enqueue(word = w2)
        q.dequeue()
        self.assertEqual(q.queue.count(w1), 0 , 'Dequeue does not work properly')
        
    def testSizeOfQ(self):
        q = qu.Queue()
        w1 = wd.Word(address = 22)
        w2 = wd.Word(address = 3)
        q.enqueue(word = w1)
        q.enqueue(word = w2)
        self.assertEqual(q.size(), 2 , 'Size does not work properly')
        
    
    