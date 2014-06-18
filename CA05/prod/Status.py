'''
Created on Mar 27, 2014

@author: Saranya Sadasivam
'''
import Word as w
class Status(w.Word):
    def __init__(self, address):
        w.Word.__init__(self,address)
        self.requestService = False
        self.messageError = False
        self.busy = False
    
    def getTerminalAddress(self):
        return w.Word.getTerminalAddress(self)
    
    def setServiceRequest(self):
        if self.requestService == True:
            return True
        else:
            self.requestService = True
            return False
        
    def isServiceRequested(self):
        if self.requestService == True:
            return True
        else:
            return False
        
    def setMessageError(self):
        if self.messageError == True:
            return True
        else:
            self.messageError = True
            return False
        
    def isMessageError(self):
        if self.messageError == True:
            return True
        else:
            return False
        
    def setBusy(self):
        if self.busy == True:
            return True
        else:
            self.busy = True
            return False
        
    def isBusy(self):
        if self.busy == True:
            return True
        else:
            return False
        