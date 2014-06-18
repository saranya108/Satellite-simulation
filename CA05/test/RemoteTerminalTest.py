'''
Created on Apr 5, 2014
@author: Saranya Sadasivams
'''
import unittest
import CA05.prod.RemoteTerminal as rt
import CA05.prod.Command as com
import CA05.prod.Data as dt
import CA05.prod.Status as st
import CA05.prod.Bus as bs


class Test(unittest.TestCase):
    def testInitExists(self):
        r = rt.RemoteTerminal(address = 2)
        assert "__init__" in dir(r), 'Method by name __init__ does not exists'
    
    def testReadBusExists(self):
        r = rt.RemoteTerminal(address = 2)
        assert "readBus" in dir(r), 'Method by name readBus does not exists'
        
    def testGetAddressExists(self):
        r = rt.RemoteTerminal(address = 2)
        assert "getAddress" in dir(r), 'Method by name getAddress does not exists'
        
    def testRTInstantiationValidReturnType(self):
        r = rt.RemoteTerminal(address = 2)
        assert isinstance(r, rt.RemoteTerminal), 'Remote terminal not instantiated properly'
        
    def testRTInstantiationValidAddress(self):
        r = rt.RemoteTerminal(address = 2)
        self.assertEqual(r.address, 2, 'Remote terminal not instantiated properly')
        
    def testRTInstantiationNoParamErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal)
        
    def testRTInstantiationNoParamErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal)
        
    def testRTInstantiationAlphaNumericErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,('a'))
        
    def testRTInstantiationAlphaNumericErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,('a'))
        
    def testRTInstantiationNegativeErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,(-1))
        
    def testRTInstantiationNegativeErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,(-1))
        
    def testRTInstantiationInvalidLErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,(0))
        
    def testRTInstantiationInvalidLErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,(0))
    
    def testRTInstantiationValidLReturnType(self):
        r = rt.RemoteTerminal(address = 1)
        assert isinstance(r, rt.RemoteTerminal), 'Remote terminal not instantiated properly'
        
    def testRTInstantiationValidLReturnAddress(self):
        r = rt.RemoteTerminal(address = 1)
        self.assertEqual(r.address, 1, 'Remote terminal not instantiated properly')
        
    def testRTInstantiationDecimalErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,(1.2))
        
    def testRTInstantiationDecimalErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,(1.2))
        
    def testRTInstantiationValidHReturnType(self):
        r = rt.RemoteTerminal(address = 30)
        assert isinstance(r, rt.RemoteTerminal), 'Remote terminal not instantiated properly'
        
    def testRTInstantiationValidHAddress(self):
        r = rt.RemoteTerminal(address = 30)
        self.assertEqual(r.address, 30, 'Remote terminal not instantiated properly')
                
    def testRTInstantiationInvalidHErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,(31))
        
    def testRTInstantiationInvalidHErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,(31))
        
    def testRTInstantiationInvalidErrorType(self):
        self.assertRaises(ValueError, rt.RemoteTerminal,(32))
        
    def testRTInstantiationInvalidErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^RemoteTerminal.__init__:\s\s", rt.RemoteTerminal,(32))
          
       
    def testScenario2(self):
        rtAddress = 5
        rtSubAddress = 10
        r = rt.RemoteTerminal(address = rtAddress)
        wordCount = r.getAddress()
        c = com.Command(address = r.getAddress())
        c.setToCommandWord(address = rtSubAddress)
        c.setReceiveCommand()
        c.setWordCount(count = wordCount)
        bus = bs.Bus()
        bus.writeBus(word = c)
        for index in range(wordCount):
            bus.writeBus(word = dt.Data(payload = index))  
        rtResponse = r.readBus(bus = bus)   
        
        rWord = rtResponse.readBus()
        assert isinstance(rWord, st.Status), 'Resulting word is not status word'
        
    def testScenario3(self):
        rtAddress = 8
        rtSubAddress = 14
        r = rt.RemoteTerminal(address = rtAddress)
        wordCount = r.getAddress() 
        c = com.Command(address = r.getAddress())
        c.setToCommandWord(address = rtSubAddress)
        c.setTransmitCommand()
        c.setWordCount(count = wordCount)
        bus = bs.Bus()
        bus.writeBus(word = c)
        rtResponse = r.readBus(bus = bus)  
        
        rWord = rtResponse.readBus()
        assert isinstance(rWord, st.Status), 'Resulting word is not status word'
        self.assertEqual(rWord.isServiceRequested(), False, 'RT wants to communicate')
        
        for i in range(r.getAddress()):
            dWord = rtResponse.readBus()
            assert isinstance(dWord, dt.Data), 'Resulting word is not data word'
            self.assertEqual(dWord.getContent(), i, 'Data word not delivered in proper order')
        self.assertRaises(ValueError, rtResponse.readBus)
        
    def testScenario1And4(self):        
            rtAddress = 10
            r = rt.RemoteTerminal(address = rtAddress)
            c = com.Command(address = r.getAddress())
            c.setToModeCommand(mode = com.Command.transmitStatusWord)
            bus = bs.Bus()
            bus.writeBus(word = c)
            rtResponse = r.readBus(bus = bus)          
            
            rWord = rtResponse.readBus()
            assert isinstance(rWord, st.Status), 'Resulting word is not status word'
            try:
                self.assertEqual(rWord.isServiceRequested(), False, 'RT wants to communicate')
                print 'Test scenario 1 was tested'
            except Exception:
                print 'Test scenario 4 was tested'
                self.assertEqual(rWord.isServiceRequested(), True, 'RT does not want to communicate')
                c1 = com.Command(address = r.getAddress())
                c1.setToModeCommand(mode = com.Command.transmitVectorWord)
                bus = bs.Bus()
                bus.writeBus(word = c1)
                rtResponse = r.readBus(bus = bus)  
                
                rWord = rtResponse.readBus()
                assert isinstance(rWord, st.Status), 'Resulting word is not status word'
                cWord = rtResponse.readBus()
                assert isinstance(cWord, com.Command), 'Resulting word is not command word'     
        
    def testGetAddressReturnType(self):
        r = rt.RemoteTerminal(address = 4)
        assert isinstance(r.getAddress(), int),'getTerminalAddress does not work properly'
        
    def testGetAddressReturnValue(self):
        r = rt.RemoteTerminal(address = 4)
        self.assertEqual(r.getAddress(), 4, 'getTerminalAddress does not work properly')
    