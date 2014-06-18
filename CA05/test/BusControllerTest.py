'''
Created on Apr 21, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.BusController as busC
import CA05.prod.Satellite as sat
import CA05.prod.RemoteTerminal as remT

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
         
    def testBusControllerInstantiationReturnType(self):
        bc = busC.BusController()
        assert(isinstance(bc, busC.BusController))

    def testBusControllerInstantiationStatusChange(self):
        bc = busC.BusController()
        self.assertEqual(bc.rtList.__len__(), 0)

    def testSetPollFrameNoParamsReturnValue(self):
        bc = busC.BusController()
        self.assertEqual(bc.setPollFrame(), 0)
        
    def testSetPollFrameEmptyrtListReturnValue(self):
        bc = busC.BusController()
        rtList = []
        self.assertEqual(bc.setPollFrame(rtList), 0)
        
    def testSetPollFrameOnertListReturnValue01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        rtList = [1]
        self.assertEqual(bc.setPollFrame(rtList), 1)    
        
    def testSetPollFrameOnertListReturnValue02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=15))
        rtList = [15]
        self.assertEqual(bc.setPollFrame(rtList), 1)  
    
    def testSetPollFrameOnertListReturnValue03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=30))
        rtList = [30]
        self.assertEqual(bc.setPollFrame(rtList), 1)  
        
    def testSetPollFrameTwortListReturnValue01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=2))
        rtList = [1, 2]
        self.assertEqual(bc.setPollFrame(rtList), 2)
        
    def testSetPollFrameTwortListReturnValue02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=15))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=29))
        rtList = [15, 29]
        self.assertEqual(bc.setPollFrame(rtList), 2)
        
    def testSetPollFrameFourrtListReturnValue(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=6))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=27))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=29))
        rtList = [1, 6, 27, 29]
        self.assertEqual(bc.setPollFrame(rtList), 4)
        
    def testSetPollFrameRepeatrtListReturnValue01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rt = remT.RemoteTerminal(address=1)
        s.addRemoteTerminal(rt)
        rtList = [1, 1]
        self.assertEqual(bc.setPollFrame(rtList), 2)
        
    def testSetPollFrameRepeatrtListReturnValue02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=30))
        rtList = [30, 30, 30]
        self.assertEqual(bc.setPollFrame(rtList), 3)    
        
    def testSetPollFrameInvalidrtListErrorType01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [0]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [0]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
        
    def testSetPollFrameInvalidrtListErrorType02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = ['a']
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = ['a']
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameInvalidrtListErrorType03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [1.2]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [1.2]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameInvalidrtListErrorType04(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [-1]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage04(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [-1]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameInvalidrtListErrorType05(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [31]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage05(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [31]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameInvalidrtListErrorType06(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [56, 44]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameInvalidrtListErrorMessage06(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [56, 44]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameWithNonExistingRTErrorType01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [1]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameWithNonExistingRTErrorMessage01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        rtList = [1]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))
        
    def testSetPollFrameWithNonExistingRTErrorType02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=6))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=8))
        rtList = [1, 4, 6, 6, 8]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameWithNonExistingRTErrorMessage02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=6))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=8))
        rtList = [1, 4, 6, 6, 8]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))   
 
    def testSetPollFrameWithNonExistingRTErrorType03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=4))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=8))
        rtList = [1, 4, 6, 6, 8]
        self.assertRaises(ValueError, bc.setPollFrame, (rtList))
         
    def testSetPollFrameWithNonExistingRTErrorMessage03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=1))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=4))
        s.addRemoteTerminal(rt=remT.RemoteTerminal(address=8))
        rtList = [1, 4, 6, 6, 8]
        self.assertRaisesRegexp(Exception, "^BusController.setPollFrame:\s\s" , bc.setPollFrame, (rtList))   
        
    def testPollReturnValue01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[])
        self.assertEqual(bc.poll(), 5, 'Buscontroller does not poll properly')
         
    def testPollAscOrder01(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[])
        bc.poll()
        self.assertEqual(sorted(bc.remoteTerminals), bc.polledTerminals, 'Buscontroller does not poll properly')
        
    def testPollReturnValue02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 31):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[])
        self.assertEqual(bc.poll(), 30, 'Buscontroller does not poll properly')
         
    def testPollAscOrder02(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(0, 30, -1):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[])
        bc.poll()
        self.assertEqual(sorted(bc.remoteTerminals), bc.polledTerminals, 'Buscontroller does not poll properly')
    
    def testPollReturnValue03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        bc.setPollFrame(rtList=[])
        self.assertEqual(bc.poll(), 0, 'Buscontroller does not poll properly')
        
    def testPollPolled03(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        bc.setPollFrame(rtList=[])
        bc.poll()
        self.assertEqual(bc.polledTerminals, [], 'Buscontroller does not poll properly')
        
    def testPollReturnValue04(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2])
        self.assertEqual(bc.poll(), 2, 'Buscontroller does not poll properly')
        
    def testPollReturnValue05(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 2, 2])
        self.assertEqual(bc.poll(), 2, 'Buscontroller does not poll properly')
        
    def testPollReturnValue06(self):
        s = sat.Satellite()
        bc = busC.BusController()
        s.setBusController(bc)
        for i in range(1, 6):
            s.addRemoteTerminal(rt=remT.RemoteTerminal(address=i))
        bc.setPollFrame(rtList=[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3])
        self.assertEqual(bc.poll(), 3, 'Buscontroller does not poll properly')

    def test100_010_ShouldPollSpecifiedRt(self):
        theBC = busC.BusController()
        self.sat.setBusController(theBC)
        theBC.setPollFrame([self.rt1.getAddress()])
        self.assertEquals(1, theBC.poll())
        
    def test100_020_ShouldPollAllRts(self):
        theBC = busC.BusController()
        self.sat.setBusController(theBC)
        self.assertEquals(3, theBC.poll())
