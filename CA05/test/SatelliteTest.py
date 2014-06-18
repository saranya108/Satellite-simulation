'''
Created on Apr 22, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Satellite as sat
import CA05.prod.BusController as busC
import CA05.prod.RemoteTerminal as remT
import CA05.prod.Bus as b

class Test(unittest.TestCase):
    def setUp(self):
        self.sat = sat.Satellite()
        self.rt1 = remT.RemoteTerminal(1)
        self.rt2 = remT.RemoteTerminal(2)
        self.rt3 = remT.RemoteTerminal(3)
        self.rt4 = remT.RemoteTerminal(4)
        self.sat.addRemoteTerminal(self.rt1)
        self.sat.addRemoteTerminal(self.rt2)
        self.sat.addRemoteTerminal(self.rt3)
        self.bus = b.Bus()


    def testSatelliteInstantiationReturnType(self):
        s = sat.Satellite();
        assert(isinstance(s, sat.Satellite))
        
    def testSatelliteInstantiationStatusChange01(self):
        s = sat.Satellite();
        self.assertEqual(s.busController, None, 'Satellite has some bus controllers on instantiation')
     
    def testSatelliteInstantiationStatusChange02(self):
        s = sat.Satellite();
        self.assertEqual(s.bus, None, 'Satellite has some buses on instantiation')   
        
    def testSatelliteInstantiationStatusChange03(self):
        s = sat.Satellite();
        self.assertEqual(s.remoteTerminals.__len__(), 0, 'Satellite has some remote terminals on instantiation')
    
    def testSetBusControllerFirstReturnType01(self):
        s = sat.Satellite();
        bc = busC.BusController()
        s.setBusController(bc)
        self.assertEqual(s.busController, bc, 'setBusController does not set bus controller')

    def testSetBusControllerFirstReturnType02(self):
        s = sat.Satellite();
        bc = busC.BusController()
        self.assertEqual(s.setBusController(bc), True, 'setBusController does not set bus controller')
        
    def testSetBusControllerSecondReturnType01(self):
        s = sat.Satellite();
        bc = busC.BusController()
        s.setBusController(bc)
        bc1 = busC.BusController()
        s.setBusController(bc1)
        self.assertEqual(s.busController, bc1, 'setBusController does not set bus controller')

    def testSetBusControllerSecondReturnType02(self):
        s = sat.Satellite();
        bc = busC.BusController()
        s.setBusController(bc)
        bc1 = busC.BusController()
        self.assertEqual(s.setBusController(bc1), False, 'setBusController does not set bus controller')
        
    def testSetBusControllerInvalidBCErrorType01(self):
        s = sat.Satellite();
        self.assertRaises(ValueError , s.setBusController, (1))
        
    def testSetBusControllerInvalidBCErrorMessage01(self):
        s = sat.Satellite();
        self.assertRaisesRegexp(Exception, "^Satellite.setBusController:\s\s" , s.setBusController, (1))
        
    def testSetBusControllerInvalidBCErrorType02(self):
        s = sat.Satellite();
        self.assertRaises(ValueError , s.setBusController)
        
    def testSetBusControllerInvalidBCErrorMessage02(self):
        s = sat.Satellite();
        self.assertRaisesRegexp(Exception, "^Satellite.setBusController:\s\s" , s.setBusController)
        
    def testAddRTFirstReturnType01(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=1);
        s.addRemoteTerminal(rt)
        self.assertEqual(s.remoteTerminals.__contains__(rt), True, 'addRemoteTerminal does not set remote terminal')

    def testAddRTFirstReturnType02(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=1);
        self.assertEqual(s.addRemoteTerminal(rt), 1, 'addRemoteTerminal does not set remote terminal')
        
    def testAddRTSecondReturnType01(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=1);
        s.addRemoteTerminal(rt)
        rt1 = remT.RemoteTerminal(address=2);
        s.addRemoteTerminal(rt1)
        self.assertEqual(s.remoteTerminals.__contains__(rt1), True, 'addRemoteTerminal does not set remote terminal')

    def testAddRTSecondReturnType02(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=1);
        s.addRemoteTerminal(rt)
        rt1 = remT.RemoteTerminal(address=2);
        self.assertEqual(s.addRemoteTerminal(rt1), 2, 'addRemoteTerminal does not set remote terminal')
        
    def testAddRTInvalidRTErrorType01(self):
        s = sat.Satellite();
        self.assertRaises(ValueError , s.addRemoteTerminal)
        
    def testAddRTInvalidRTErrorMessage01(self):
        s = sat.Satellite();
        self.assertRaisesRegexp(Exception, "^Satellite.addRemoteTerminal:\s\s" , s.addRemoteTerminal)
    
    def testAddRTInvalidRTErrorType02(self):
        s = sat.Satellite();
        self.assertRaises(ValueError , s.addRemoteTerminal, (2))
        
    def testAddRTInvalidRTErrorMessage02(self):
        s = sat.Satellite();
        self.assertRaisesRegexp(Exception, "^Satellite.addRemoteTerminal:\s\s" , s.addRemoteTerminal, (2))
        
    def testAddRTInvalidRTErrorType03(self):
        s = sat.Satellite();
        for i in range(1, 31):
            rt = remT.RemoteTerminal(address=i)
            s.addRemoteTerminal(rt)
        rtfinal = remT.RemoteTerminal(address=2)
        self.assertRaises(ValueError, s.addRemoteTerminal, (rtfinal))
        
    def testAddRTInvalidRTErrorMessage03(self):
        s = sat.Satellite();
        for i in range(1, 31):
            rt = remT.RemoteTerminal(address=i)
            s.addRemoteTerminal(rt)
        rtfinal = remT.RemoteTerminal(address=2)
        self.assertRaisesRegexp(Exception, "^Satellite.addRemoteTerminal:\s\s" , s.addRemoteTerminal, (rtfinal))
         
    def testAddRTInvalidRTErrorType04(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=2)
        s.addRemoteTerminal(rt)
        self.assertRaises(ValueError , s.addRemoteTerminal, (rt))
         
    def testAddRTInvalidRTErrorMessage04(self):
        s = sat.Satellite();
        rt = remT.RemoteTerminal(address=2)
        s.addRemoteTerminal(rt)
        self.assertRaisesRegexp(Exception, "^Satellite.addRemoteTerminal:\s\s" , s.addRemoteTerminal, (rt)) 
        
    def testGetRTReturnValue01(self):
        s = sat.Satellite();
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=2))
        retVal = s.getRemoteTerminal()
        self.assertEqual(retVal.__len__(), 2, 'getRemoteTerminal does not get remote terminal')
        
    def testGetRTReturnValue02(self):
        s = sat.Satellite();
        retVal = s.getRemoteTerminal()
        self.assertEqual(retVal.__len__(), 0, 'getRemoteTerminal does not get remote terminal')
        
    def testLaunchReturnValue01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        self.assertEqual(s.launch(frameCount=0), 5, 'launch does not launch buscontroller')
        
    def testLaunchPolledNo01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        s.launch(frameCount=0)
        self.assertEqual(s.polled, 1, 'launch does not launch buscontroller')
        
    def testLaunchReturnValue02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        self.assertEqual(s.launch(frameCount=1), 5, 'launch does not launch buscontroller')
    
    def testLaunchPolledNo02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        s.launch(frameCount=1)
        self.assertEqual(s.polled, 1, 'launch does not launch buscontroller')
        
    def testLaunchReturnValue03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        self.assertEqual(s.launch(), 5, 'launch does not launch buscontroller')
   
    def testLaunchPolledNo03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        s.launch()
        self.assertEqual(s.polled, 1, 'launch does not launch buscontroller')
        
    def testLaunchReturnValue04(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        self.assertEqual(s.launch(frameCount=2), 5, 'launch does not launch buscontroller')
        
    def testLaunchPolledNo04(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 3, 4, 5])
        s.launch(frameCount=2)
        self.assertEqual(s.polled, 2, 'launch does not launch buscontroller')
        
    def testLaunchReturnValue05(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        self.assertEqual(s.launch(frameCount=5), 2, 'launch does not launch buscontroller')
        
    def testLaunchPolledNo05(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        s.launch(frameCount=5)
        self.assertEqual(s.polled, 5, 'launch does not launch buscontroller')
        
    def testLaunchErrorType01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        self.assertRaises(ValueError, s.launch, (-1))
        
    def testLaunchErrorMessage01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        s.launch(frameCount=5)
        self.assertRaisesRegexp(Exception, "^Satellite.launch:\s\s" , s.launch, (-1))
        
    def testLaunchErrorType02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        self.assertRaises(ValueError, s.launch, (1.2))
        
    def testLaunchErrorMessage02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 3):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        s.launch(frameCount=5)
        self.assertRaisesRegexp(Exception, "^Satellite.launch:\s\s" , s.launch, (1.2))
        
        
    def testScenario(self):
        # Create some remote terminals
        rt1 = remT.RemoteTerminal(1)
        rt2 = remT.RemoteTerminal(2)
        rt3 = remT.RemoteTerminal(3)
        
        # Create a bus controller
        bc = busC.BusController()
        
        # Create a satellite and install the subsystems
        s = sat.Satellite()
        s.setBusController(bc)
        s.addRemoteTerminal(rt1)
        s.addRemoteTerminal(rt2)
        s.addRemoteTerminal(rt3)
        
        # Tell the bus controller the order in which to poll remote terminals
        pollFrame = [1, 2, 2, 3]
        bc.setPollFrame(pollFrame)
        
        # Start the subsystems
        s.launch()                   
                                    
#         The subsystems operate under the supervision of the bus controller as follows:                            
#         for each remote terminal in the poll frame:                            
#          - the bus controller requests the remote terminal's status via a status command written to the bus                            
#          - the bus controller takes no action if the remote terminal responds with "no service required"                            
#          - if the remote terminal responds with "service required", the bus controller sends a "transmit vector word" command to the remote terminal.                            
#          - the remote terminal repeats its status word and also transmits as data the command it needs the bus controller to issue, such as a request to transmit or receive.                            
#          - the bus controller places the command word (along with data that accompanies the command) on the bus and the appropriate remote terminal responds                            
 
        # Test launch 
    def test100_010_ShouldDetermineApproximateBusBehavior(self):
        theBC = busC.BusController()
        self.sat.setBusController(theBC)
        theBC.setPollFrame([self.rt1.getAddress()])
# polling rt1:
# Because this is a blackbox test at the satellite level, we don't have 
# direct visibility into exactly what is being written to the bus, 
# only how many words have been written. (NB: We have unit tests 
# at the component level that, presumably, pass. This gives us 
# confidence that the components work in isolation. What we 
# want to do now is get some degree of confidence that they work 
# when integrated together.)
# What we know:
# * the original specs say that a remote terminal has p(no service) = .5 
# and p(service requested) = .5
# * if service is requested, then p(transmit) = .5 and p(receive) = .5
# * overall, this means that p(no service) = .5, p(transmit) = .25, 
# p(receive)=.25
#
# * our scenarios specify that a remote terminal transmits/receives n words, 
# where n is the address
# 
# Given this information:
# 1. rt1 requests no service 
# BC requests status = 1 word
# RT responds with status = 1 word
# = 2 words
#
# 2. rt1 requests service, service is transmit command
# BC requests status = 1 word
# RT responds with status = 1 word
# BC requests vector word = 1 word
# RT responds with status + transmit command = 2 words
# BC issues transmit command = 1 word
# RT responds with status + 1 data word = 2 words
# = 8 words
# 
# 3. rt1 requests service, service is receive command
# BC requests status = 1 word
# RT responds with status = 1 word
# BC requests vector word = 1 word
# RT responds with status + receive command = 2 words
# BC issues receive command + 1 data word = 2 word
# RT responds with status = 1 words
# = 8 words
#
# 
# Each time we run BusController.poll(), we will get 1 in return. 
# This doesn't give us much insight.
#
# But, we can run run Satellite.launch() and get an idea of whether our 
# software is approximating our expected behavior by examining the number 
# of words written to the bus. Given the probabilities above,
# we expect, on the average, 5 words written each time RT1 is polled.
# Alternative 1: Satellite.launch(n) should return n*5
        sampleSize = 10000
        averageWordCount = 5
        expectedCount = float(sampleSize * averageWordCount)
        actualCount = float(self.sat.launch(sampleSize))
        self.assertAlmostEquals(abs(actualCount-expectedCount)/expectedCount, 1.0, 1)  
# Alternative 2: Call Satellite.launch(1) n times. 
# 2 should be returned half the time, 8 the other half. 
        sampleSize = 10000
        twoWordTally = 0
        eightWordTally = 0
        for samples in range(sampleSize):
            result = self.sat.launch(1)
        if (result == 2):
            twoWordTally += 1
        elif (result == 8):
            eightWordTally +=1
        else:
            self.fail()
            self.assertAlmostEquals(float(twoWordTally)/float(eightWordTally), 1.0, 1)