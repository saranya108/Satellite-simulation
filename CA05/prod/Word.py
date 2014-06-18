'''
Created on Mar 27, 2014

@author: Saranya Sadasivam
'''

class Word(object):
    def __init__(self,address = None):
        if address == None:
            raise ValueError(self.__class__.__name__+".__init__:  Terminal address not provided") 
        elif not isinstance(address, int):
            raise ValueError(self.__class__.__name__+".__init__:  Terminal address is not an integer") 
        elif address <= 0 or address >= 31:
            raise ValueError(self.__class__.__name__+".__init__:  Terminal address is not in valid range 0 < address < 31") 
        else:
            self.address = address
        
    def getTerminalAddress(self):
        return self.address

    