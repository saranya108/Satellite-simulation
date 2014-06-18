'''
Created on Apr 21, 2014
@author: Saranya Sadasivam
'''
import Command as com
import Bus as bs
import Data as d
import Status as s

class BusController(object):

    def __init__(self):
        # list of remote terminals to be polled
        self.rtList = []
        # list of remote terminals in the satellite
        self.remoteTerminals = []
        # list of remote terminals done with polling
        self.polledTerminals = []
        # bus object through which communication takes place
        self.bus = None
   
    # associates bus to this buscontroller instance
    def setBus(self, bus):
        self.bus = bus
        
    def setPollFrame(self, rtList = None):
        if rtList == None or rtList == []:
            return 0
        else:
            l = rtList.__len__()
            for i in range(l):
                if not isinstance(rtList[i], int):
                    raise ValueError("BusController.setPollFrame:  rtList does not have integers")
                
                elif rtList[i] <= 0 or rtList[i] >= 31:
                    raise ValueError("BusController.setPollFrame:  rtList does not have entry in valid range 0 < address < 31")
                
                elif self.checkContainsRT(rtList[i]) is None:
                    raise ValueError("BusController.setPollFrame:  rtList does not exist in satellite")
                
                else:
                    self.rtList = rtList;
            return self.rtList.__len__()
  
  
    # checks if remote terminal address exists in the satellite, if so returns its instance given its address
    def checkContainsRT(self,searchAdd):
        rl = self.remoteTerminals
        
        for i in rl:
            if searchAdd == i.getAddress():
                return i
        return None


    def setRemoteTerminals(self,remoteTerminals):
        self.remoteTerminals = remoteTerminals
   
    # fetches the existing remote terminals in a ascending order
    def getRTInAscOrder(self):
        # list contains only remote terminal addresses
        tempList = []
        # reversed remote terminal instance list
        retList = []
        
        for i in self.remoteTerminals:
            tempList.append(i.getAddress())
            
        # sorts the list in place
        tempList.sort(cmp=None, key=None, reverse=False)       
        
        for j in tempList:
            retList.append(self.checkContainsRT(j))
        return retList
            
    def poll(self):
        if self.rtList == [] and self.remoteTerminals.__len__() > 0:
            self.polledTerminals = []
            # for every remote terminal poll and then add to polled list
            for i in self.getRTInAscOrder():
                self.pollTerminal(i)
                self.polledTerminals.append(i)
            return self.remoteTerminals.__len__()
        
        elif self.rtList == [] and self.remoteTerminals.__len__() == 0:
            return 0
        
        else:
            # makes sure duplicate entries are considered once
            for i in set(self.rtList):
                self.pollTerminal(self.checkContainsRT(i))
            return set(self.rtList).__len__() 
  
    # polls the specified terminal
    def pollTerminal(self,polledRt):
        # creates a command word requesting status to current remote terminal
        c = com.Command(polledRt.getAddress())
        c.setToModeCommand(com.Command.transmitStatusWord)
        b = self.bus
        b.writeBus(c)
        
        rtResponse = polledRt.readBus(b)
        rWord = rtResponse.readBus()
        
        if isinstance(rWord, s.Status): 
            # if service is requested by the terminal    
            if rWord.isServiceRequested() == True:
                # creates a command word requesting terminal for vector word
                c = com.Command(polledRt.getAddress())
                c.setToModeCommand(com.Command.transmitVectorWord)
                b.writeBus(c)
                
                rtResponse = polledRt.readBus(b)          
                rWord = rtResponse.readBus()
                cWord = rtResponse.readBus()
                
                if isinstance(cWord, com.Command) and not cWord.isModeCommand():
                    # processes command word returned by the terminal based on it being a transmit or receive command word
                    cAdd = cWord.getSubAddress()
                    wc = cWord.getWordCount()
                    
                    # checks of the other terminal exists in the satellite before communicating with it
                    if self.checkContainsRT(cAdd) is not None:
                        c = com.Command(cAdd)
                        c.setToCommandWord(cAdd)
                        # command word is a transmit command, sends transmit command and reads bus wordCount times
                        
                        if cWord.isTransmitCommand():
                            c.setTransmitCommand()
                            c.setWordCount(wc)
                            b.writeBus(c)
                            
                            rtResponse = self.checkContainsRT(cAdd).readBus(b)
                            sWord = rtResponse.readBus()
                            for i in range(wc):
                                b.readBus()
                                
                        # for receive command, sends receive command and writes wordCount words onto the bus
                        if not cWord.isTransmitCommand():
                            c.setReceiveCommand()
                            c.setWordCount(wc)
                            b.writeBus(c)
                            
                            for i in range(wc):
                                b.writeBus(d.Data(i))
                            rtResponse = self.checkContainsRT(cAdd).readBus(b)
                        