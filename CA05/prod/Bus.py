'''
Created on Mar 27, 2014
@author: Saranya Sadasivam
'''
import Queue as q
import Word as w
class Bus(object):
    def __init__(self):
        self.bus = q.Queue();
    
    def writeBus(self,word = None):
        if word == None:
            raise ValueError("Bus.writeBus:  Word is not provided") 
        elif not isinstance(word, w.Word):
            raise ValueError("Bus.writeBus:  Word is not valid")
        else:
            self.bus.enqueue(word);
            return self.bus.size();
        
    def readBus(self):
        if self.bus.isEmpty():
            raise ValueError("Bus.readBus:  Bus is empty") 
        else:
            return self.bus.dequeue()