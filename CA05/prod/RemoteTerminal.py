'''
Created on Mar 27, 2014
@author: Saranya Sadasivam
'''
import Bus as b
import Status as s
import Command as c
import Data as d
import random

class RemoteTerminal(object):
    def __init__(self, address = None):
        if address is None:
            raise ValueError("RemoteTerminal.__init__:  Address is not provided") 
        elif not isinstance(address, int):
            raise ValueError("RemoteTerminal.__init__:  Address is not an integer") 
        elif address <= 0 or address >= 31:
            raise ValueError("RemoteTerminal.__init__:  Address not in valid range 0 < address < 31") 
        else:
            self.address = address
        
    def readBus(self, bus = None):
        if bus is None:
            raise ValueError("RemoteTerminal.readBus:  Bus is not provided") 
        elif not isinstance(bus, b.Bus):
            raise ValueError("RemoteTerminal.readBus:  Bus is invalid") 
        elif bus.bus.isEmpty():
            raise ValueError("RemoteTerminal.readBus:  Bus is empty") 
        else:
            # reads a word from bus
            word = bus.readBus()
            if isinstance(word, c.Command):
                # if word is address to current rt terminal
                if word.getTerminalAddress() is self.getAddress():
                    # if command is a command word
                    if not word.isModeCommand():
                        # if command is to transmit or receive data
                        # if command word is to receive
                        if not word.isTransmitCommand():
                            # reads wordCount no. of times from the bus
                            for i in range(word.getWordCount()):
                                bus.readBus()
                            # create status word and send it on bus
                            response = s.Status(self.getAddress())
                            bus.writeBus(response)
                        # if command is to transmit
                        elif word.isTransmitCommand():
                            # write status word onto bus
                            response = s.Status(self.getAddress())
                            bus.writeBus(response)
                            # write wordCount no. of data words
                            for i in range(word.getWordCount()):
                                bus.writeBus(d.Data(i))
                    # if command is a mode command
                    else:
                        # get the mode code
                        mCode = word.getModeCode()
                        # if mode code is to transmit status
                        if mCode is c.Command.transmitStatusWord: 
                            # randomly transmit status as either no service requested or service is requested
                            randResponse = random.randint(1,2)
                            # when no service is requested
                            if randResponse == 1:
                                response = s.Status(self.getAddress())
                                bus.writeBus(response)
                            # when service is requested
                            else:
                                response = s.Status(self.getAddress())
                                response.setServiceRequest()
                                bus.writeBus(response)
                        # if mode code is to transmit vector word
                        elif mCode is c.Command.transmitVectorWord:
                            # write status word to bus
                            response = s.Status(self.getAddress())
                            bus.writeBus(response)
                            # randomly pick one of the other existing remote terminals 
                            ranAdd = random.randint(1,30)
                            # make sure a remote terminal does not communicate with itself
                            while ranAdd == self.getAddress():
                                ranAdd = random.randint(1,30)
                            # randomly create a receive or a transmit command word and send on bus
                            randTR = random.randint(1,2)
                            command = c.Command(self.getAddress())
                            command.setToCommandWord(ranAdd)
                            # command word to transmit
                            if randTR == 1:
                                command.setTransmitCommand()
                                # randomly choosing wordCount 
                                command.setWordCount(random.randint(1,5))
                                bus.writeBus(command)
                            else:
                                command.setReceiveCommand()
                                wc = random.randint(1,5)
                                command.setWordCount(wc)
                                bus.writeBus(command)
                                for index in range(wc):
                                    bus.writeBus(d.Data(index))  
        return bus      
            
    def getAddress(self):
        return self.address