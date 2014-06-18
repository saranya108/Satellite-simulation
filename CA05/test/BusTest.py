'''
Created on Apr 5, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Bus as bs
import CA05.prod.Command as com
import CA05.prod.Data as dt
import CA05.prod.Status as st

class Test(unittest.TestCase):
    def testInitExists(self):
        b = bs.Bus()
        assert "__init__" in dir(b), 'Method by name __init__ does not exists'
        
    def testWriteBusExists(self):
        b = bs.Bus()
        assert "writeBus" in dir(b), 'Method by name writeBus does not exists'
        
    def testReadBusExists(self):
        b = bs.Bus()
        assert "readBus" in dir(b), 'Method by name readBus does not exists'
        
    def testBusInstantiationReturnType(self):
        b = bs.Bus()
        assert isinstance(b, bs.Bus), 'Bus is not instantiated properly'
       
    def testBusInstantiationReturnValue(self):
        b = bs.Bus()
        self.assertEqual(b.bus.size(), 0, 'Bus is not instantiated properly')
       
    def testWriteBusCommandFirstReturnValue(self):
        b = bs.Bus()
        c = com.Command(address = 3)
        self.assertEqual(b.writeBus(word = c), 1, 'Bus is not instantiated properly')
        
    def testWriteBusCommandFirstStateChange(self):
        b = bs.Bus()
        c = com.Command(address = 3)
        b.writeBus(word = c)
        self.assertEqual(b.bus.size(), 1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c, 'Bus is not instantiated properly')
        
    def testWriteBusCommandSecondReturnValue(self):
        b = bs.Bus()
        c1 = com.Command(address = 3)
        b.writeBus(word = c1)
        c2 = com.Command(address = 5)
        self.assertEqual(b.writeBus(word = c2), 2, 'Bus is not instantiated properly')
        
    def testWriteBusCommandSecondStateChange(self):
        b = bs.Bus()
        c1 = com.Command(address = 3)
        b.writeBus(word = c1)
        c2 = com.Command(address = 5)
        b.writeBus(word = c2)
        self.assertEqual(b.bus.size(), 2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c2, 'Bus is not instantiated properly')
        
    def testWriteBusCommandThirdReturnValue(self):
        b = bs.Bus()
        c1 = com.Command(address = 3)
        b.writeBus(word = c1)
        c2 = com.Command(address = 5)
        b.writeBus(word = c2)
        c3 = com.Command(address = 6)
        self.assertEqual(b.writeBus(word = c3), 3, 'Bus is not instantiated properly')
        
    def testWriteBusCommandThirdStateChange(self):
        b = bs.Bus()
        c1 = com.Command(address = 3)
        b.writeBus(word = c1)
        c2 = com.Command(address = 5)
        b.writeBus(word = c2)
        c3 = com.Command(address = 6)
        b.writeBus(word = c3)
        self.assertEqual(b.bus.size(), 3, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), c3, 'Bus is not instantiated properly')    
           
    def testWriteBusDataFirstReturnValue(self):
        b = bs.Bus()
        d = dt.Data(payload = 3)
        self.assertEqual(b.writeBus(word = d), 1, 'Bus is not instantiated properly')
        
    def testWriteBusDataFirstStateChange(self):
        b = bs.Bus()
        d = dt.Data(payload = 3)
        b.writeBus(word = d)
        self.assertEqual(b.bus.size(), 1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d, 'Bus is not instantiated properly')
        
    def testWriteBusDataSecondReturnValue(self):
        b = bs.Bus()
        d1 = dt.Data(payload = 3)
        b.writeBus(word = d1)
        d2 = dt.Data(payload = 5)
        self.assertEqual(b.writeBus(word = d2), 2, 'Bus is not instantiated properly')
        
    def testWriteBusDataSecondStateChange(self):
        b = bs.Bus()
        d1 = dt.Data(payload = 3)
        b.writeBus(word = d1)
        d2 = dt.Data(payload = 5)
        b.writeBus(word = d2)
        self.assertEqual(b.bus.size(), 2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d2, 'Bus is not instantiated properly')
        
    def testWriteBusDataThirdReturnValue(self):
        b = bs.Bus()
        d1 = dt.Data(payload = 3)
        b.writeBus(word = d1)
        d2 = dt.Data(payload = 5)
        b.writeBus(word = d2)
        d3 = dt.Data(payload = 6)
        self.assertEqual(b.writeBus(word = d3), 3, 'Bus is not instantiated properly')
        
    def testWriteBusDataThirdStateChange(self):
        b = bs.Bus()
        d1 = dt.Data(payload = 3)
        b.writeBus(word = d1)
        d2 = dt.Data(payload = 5)
        b.writeBus(word = d2)
        d3 = dt.Data(payload = 6)
        b.writeBus(word = d3)
        self.assertEqual(b.bus.size(), 3, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), d3, 'Bus is not instantiated properly')
        
    def testWriteBusStatusFirstReturnValue(self):
        b = bs.Bus()
        s = st.Status(address = 3)
        self.assertEqual(b.writeBus(word = s), 1, 'Bus is not instantiated properly')
        
    def testWriteBusStatusFirstStateChange(self):
        b = bs.Bus()
        s = st.Status(address = 3)
        b.writeBus(word = s)
        self.assertEqual(b.bus.size(), 1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s, 'Bus is not instantiated properly')
        
    def testWriteBusStatusSecondReturnValue(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        self.assertEqual(b.writeBus(word = s2), 2, 'Bus is not instantiated properly')
        
    def testWriteBusStatusSecondStateChange(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        self.assertEqual(b.bus.size(), 2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s2, 'Bus is not instantiated properly')
        
    def testWriteBusStatusThirdReturnValue(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        s3 = st.Status(address = 6)
        self.assertEqual(b.writeBus(word = s3), 3, 'Bus is not instantiated properly')
        
    def testWriteBusStatusThirdStateChange(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        s3 = st.Status(address = 6)
        b.writeBus(word = s3)
        self.assertEqual(b.bus.size(), 3, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s1, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s2, 'Bus is not instantiated properly')
        self.assertEqual(b.bus.dequeue(), s3, 'Bus is not instantiated properly')
        
    def testWriteBusNoParamErrorType(self):
        b = bs.Bus()
        self.assertRaises(ValueError, b.writeBus)
        
    def testWriteBusNoParamErrorMessage(self):
        b = bs.Bus()
        self.assertRaisesRegexp(Exception, "^Bus.writeBus:\s\s", b.writeBus)
        
    def testWriteBusAlphaNumericErrorType(self):
        b = bs.Bus()
        self.assertRaises(ValueError, b.writeBus,('a'))
        
    def testWriteBusAlphaNumericErrorMessage(self):
        b = bs.Bus()
        self.assertRaisesRegexp(Exception, "^Bus.writeBus:\s\s", b.writeBus,('a'))
        
    def testWriteBusNegativeErrorType(self):
        b = bs.Bus()
        self.assertRaises(ValueError, b.writeBus,(1))
        
    def testWriteBusNumberErrorMessage(self):
        b = bs.Bus()
        self.assertRaisesRegexp(Exception, "^Bus.writeBus:\s\s", b.writeBus, (1))
        
    def testReadBusNEReturnValue(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        s3 = st.Status(address = 6)
        b.writeBus(word = s3)
        self.assertEqual(b.readBus(), s1, 'readBus does not work properly')
        
    def testReadBusNEReturnType(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        s3 = st.Status(address = 6)
        b.writeBus(word = s3)
        assert isinstance(b.readBus(), st.Status), 'readBus does not work properly'
        
    def testReadBusNEStatusChange(self):
        b = bs.Bus()
        s1 = st.Status(address = 3)
        b.writeBus(word = s1)
        s2 = st.Status(address = 5)
        b.writeBus(word = s2)
        s3 = st.Status(address = 6)
        b.writeBus(word = s3)
        self.assertEqual(b.readBus(), s1, 'readBus does not work properly')
        
    def testReadBusEErrorType(self):
        b = bs.Bus()
        self.assertRaises(ValueError, b.readBus)
        
    def testReadBusEErrorMessage(self):
        b = bs.Bus()
        self.assertRaisesRegexp(Exception, "^Bus.readBus:\s\s", b.readBus)
    