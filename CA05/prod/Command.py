'''
Created on Mar 27, 2014

@author: Saranya Sadasivam
'''
import Word as w
class Command(w.Word):
    transmitStatusWord = 2
    shutDown = 4
    reset = 8
    transmitVectorWord = 12
    transmitLastCommand = 14
    wordCount = 0
    subAddress = 0
    def __init__(self, address):
        w.Word.__init__(self, address)
        self.modeCommand = True
        self.tr = False
        self.modeCode = self.transmitStatusWord
        
    def getTerminalAddress(self):
        return w.Word.getTerminalAddress(self)
    
    def setToCommandWord(self,address = None):
        self.wordCount = 0
        if address == None:
            self.subAddress = 1
        elif not isinstance(address, int):
            raise ValueError("Command.setToCommandWord:  SubAddress is not an integer") 
        elif address <= 0 or address >= 31:
            raise ValueError("Command.setToCommandWord:  SubAddress not in valid range 0 < address < 31") 
        else:
            self.subAddress = address
        if self.modeCommand == False:
            return True
        else:
            self.modeCommand = False
            return False
        
    def setToModeCommand(self, mode = None):
        if mode == None:
            self.modeCode = self.transmitStatusWord
        elif mode not in [2,4,8,12,14]:
            raise ValueError("Command.setToModeCommand:  Mode code is not of valid value")
        else:
            self.modeCode = mode
            self.subAddress = 0
        return self.modeCode
            
    def getModeCode(self):
        if not self.isModeCommand():
            raise ValueError("Command.getModeCode:  Command word is not mode command")
        else:
            return self.modeCode        
    
    def isModeCommand(self):
        return self.modeCommand
    
    def setSubAddress(self,address):
        if address == None:
            raise ValueError("Command.setSubAddress:  SubAddress is not provided") 
        elif not isinstance(address, int):
            raise ValueError("Command.setSubAddress:  SubAddress is not an integer") 
        elif address <= 0 or address >= 31:
            raise ValueError("Command.setSubAddress:  SubAddress not in valid range 0 < address < 31") 
        elif self.modeCommand == True:
            raise ValueError("Command.setSubAddress:  Command word is a mode command")
        else:
            self.subAddress = address
            return self.subAddress
        
    def getSubAddress(self):
        if self.isModeCommand():
            raise ValueError("Command.getSubAddress:  Command word is mode command")
        else:
            return self.subAddress
        
    def setWordCount(self, count = None):
        if count == None:
            raise ValueError("Command.setWordCount:  Count is not provided")
        elif not isinstance(count, int):
            raise ValueError("Command.setWordCount:  Count is not an integer")
        elif count <= 0 or count >= 31:
            raise ValueError("Command.setWordCount:  Count not in valid range 0 < address < 31")
        elif self.isModeCommand():
            raise ValueError("Command.setWordCount:  Command word is a mode command")
        else:
            self.wordCount = count
            return self.wordCount
        
    def getWordCount(self):
        if self.isModeCommand():
            raise ValueError("Command.getWordCount:  Command word is a mode command")
        else:
            return self.wordCount
        
    def setTransmitCommand(self):
        if self.tr == True:
            return True
        else:
            self.tr = True
            return False 

    def setReceiveCommand(self):
        if self.tr == False:
            return True
        else:
            self.tr = False
            return False   
    
    def isTransmitCommand(self):
        if self.tr == True:
            return True
        else:
            return False
          
    
            
        