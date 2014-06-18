'''
Created on Mar 27, 2014

@author: Saranya Sadasivam
'''
class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, word):
        self.queue.insert(0,word)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue.dequeue:  Bus is empty")
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)