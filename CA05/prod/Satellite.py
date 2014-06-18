'''
Created on Apr 22, 2014

@author: Saranya Sadasivam
'''
import BusController as busC
import RemoteTerminal as remT
import Bus as b

class Satellite(object):

    def __init__(self):
        self.busController = None
        self.bus = None
        # list of current remote terminals in the satellite
        self.remoteTerminals = []
        # list recording how many times the bus controller was polled
        self.polled = 0
        
    def setBusController(self, bc = None):
        if not isinstance(bc, busC.BusController) or bc == None:
            raise ValueError("Satellite.setBusController:  bc is not a BusController instance")
        # based on this value the method returns a true or a false
        oldVal = self.busController
        self.busController = bc
        self.bus = b.Bus()
        
        # sets remote terminals in the satellite
        bc.setRemoteTerminals(self.getRemoteTerminal())
        # associates bus to bus controller 
        bc.setBus(self.bus)
        
        if oldVal == None:
            return True
        else:
            return False
        
    def addRemoteTerminal(self,rt = None):
        rtl = self.getRemoteTerminal()
        if rt == None or rt == '' or not isinstance(rt, remT.RemoteTerminal):
            raise ValueError("Satellite.addRemoteTerminal:  rt is not a RemoteTerminal instance")
        
        elif rtl.__len__() == 30:
            raise ValueError("Satellite.addRemoteTerminal:  Only up to 30 remote terminals can be added")
        
        elif rtl.__contains__(rt):
            raise ValueError("Satellite.addRemoteTerminal:  rt is already existing")
        
        else:
            # adds remote terminal to the remote terminal list of satellite
            rtl.append(rt)
            
            # if bus controller exists the remote terminal list maintained by it is also changed
            if self.busController is not None:
                self.busController.setRemoteTerminals(rtl)
        return rtl.__len__()
    
    def getRemoteTerminal(self):
        return self.remoteTerminals
    
    def launch(self,frameCount = None):
        self.polled = 0
        if frameCount == None:
            frameCount = 1
        else:
            if not isinstance(frameCount, int) or frameCount < 0:
                raise ValueError("Satellite.launch:  frameCount is not a valid")
            
        if frameCount == 0 or frameCount == 1:
            retVal = self.busController.poll()
            self.polled += 1
            return retVal
        else:
            for i in range(frameCount):
                retVal = self.busController.poll()
                self.polled += 1
            return retVal