'''
Created on Mar 27, 2014

@author: Saranya Sadasivam
'''
import Word as w
class Data(w.Word):
    def __init__(self, payload = None):
        if payload == None:
            self.payload = 0
        elif not self.isPayloadValid(payload):
            raise ValueError("Data.__init__:  Payload is not a valid value")
        else:
            self.payload = payload
            
    def setContent(self, payload = None):
        if payload == None:
            raise ValueError("Data.setContent:  Payload value not provided")
        elif not self.isPayloadValid(payload):
            raise ValueError("Data.setContent:  Payload is not a valid value")
        else:    
            self.payload = payload
        return self.payload
    
    def isPayloadValid(self,payload = None):
        if not isinstance(payload, int):
            return False
        elif payload < 0 or payload > 65535:
            return False
        else:
            return True
            
    def getContent(self):
        return self.payload