'''
Created on Apr 1, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Status as st

class Test(unittest.TestCase):
    def testInitExists(self):
        s = st.Status(address = 2)
        assert "__init__" in dir(s), 'Method by name __init__ does not exists'
    
    def testGetTerminalAddressExists(self):
        s = st.Status(address = 2)
        assert "getTerminalAddress" in dir(s), 'Method by name getTerminalAddress does not exists'
        
    def testSetServiceRequestExists(self):
        s = st.Status(address = 2)
        assert "setServiceRequest" in dir(s), 'Method by name setServiceRequest does not exists'
        
    def testisServiceRequestedExists(self):
        s = st.Status(address = 2)
        assert "isServiceRequested" in dir(s), 'Method by name isServiceRequested does not exists'
        
    def testsetMessageErrorExists(self):
        s = st.Status(address = 2)
        assert "setMessageError" in dir(s), 'Method by name setMessageError does not exists'
        
    def testisMessageErrorExists(self):
        s = st.Status(address = 2)
        assert "isMessageError" in dir(s), 'Method by name isMessageError does not exists'
        
    def testsetBusyExists(self):
        s = st.Status(address = 2)
        assert "setBusy" in dir(s), 'Method by name setBusy does not exists'
        
    def testisBusyExists(self):
        s = st.Status(address = 2)
        assert "isBusy" in dir(s), 'Method by name isBusy does not exists'
        
    def testSWInstantiationWithValidLForReturnType(self):
        s = st.Status(address = 2)
        assert isinstance(s, st.Status), 'status is not an instantiated properly'
         
    def testSWInstantiationWithValidLForAddress(self):
        s = st.Status(address = 2)
        self.assertEqual(s.getTerminalAddress(), 2, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidLForServiceRequest(self):
        s = st.Status(address = 2)
        self.assertEqual(s.isServiceRequested(), False, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidLForMessageError(self):
        s = st.Status(address = 2)
        self.assertEqual(s.isMessageError(), False, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidLForBusy(self):
        s = st.Status(address = 2)
        self.assertEqual(s.isBusy(), False, 'status is not an instantiated properly')
        
    def testSWInstantiationWithInvalidLForErrorType(self):   
        self.assertRaises(ValueError, st.Status, (0))
        
    def testSWInstantiationWithInvalidLForErrorMessage(self): 
        self.assertRaisesRegexp(Exception, "^Status.__init__:\s\s", st.Status, (0))
        
    def testSWInstantiationWithAlphaNumericForErrorType(self): 
        self.assertRaises(ValueError, st.Status, ('a'))  
        
    def testSWInstantiationWithAlphaNumericForErrorMessage(self):   
        self.assertRaisesRegexp(Exception, "^Status.__init__:\s\s", st.Status, ('a'))
          
    def testSWInstantiationWithNegativeForErrorType(self):   
        self.assertRaises(ValueError, st.Status, (-1))  
        
    def testSWInstantiationWithNegativeForErrorMessage(self): 
        self.assertRaisesRegexp(Exception, "^Status.__init__:\s\s", st.Status, (-1))
        
    def testSWInstantiationWithInvalidHForErrorType(self):   
        self.assertRaises(ValueError, st.Status, (31))
        
    def testSWInstantiationWithInvalidHForErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Status.__init__:\s\s", st.Status, (31))
        
    def testSWInstantiationWithInvalidForErrorType(self):   
        self.assertRaises(ValueError, st.Status, (32))
        
    def testSWInstantiationWithInvalidForErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Status.__init__:\s\s", st.Status, (32))
        
    def testSWInstantiationWithValidHForReturnType(self):
        s = st.Status(address = 30)
        assert isinstance(s, st.Status), 'status is not an instantiated properly'
        
    def testSWInstantiationWithValidHForAddress(self):    
        s = st.Status(address = 30)
        self.assertEqual(s.getTerminalAddress(), 30, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidHForServiceRequest(self):
        s = st.Status(address = 30)
        self.assertEqual(s.isServiceRequested(), False, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidHForMessageError(self):
        s = st.Status(address = 30)
        self.assertEqual(s.isMessageError(), False, 'status is not an instantiated properly')
        
    def testSWInstantiationWithValidHForBusy(self):    
        s = st.Status(address = 30)
        self.assertEqual(s.isBusy(), False, 'status is not an instantiated properly')
        
    def testGetTerminalAddressForReturnType(self):
        s = st.Status(address = 30)
        assert isinstance(s.getTerminalAddress(), int),'getTerminal address does not return an integer'
        
    def testGetTerminalAddressForReturnValue(self):
        s = st.Status(address = 30)
        self.assertEqual(s.getTerminalAddress(), 30, 'getTerminal address does not return correct value')
        
    def testSetServiceRequestRepeatReturnValue(self):
        s = st.Status(address = 24)
        s.setServiceRequest()
        self.assertEqual(s.setServiceRequest(), True, 'setServiceRequest not working properly')
        
    def testSetServiceRequestRepeatStatusChange(self):
        s = st.Status(address = 24)
        s.setServiceRequest()
        s.setServiceRequest()
        self.assertEqual(s.requestService, True, 'setServiceRequest not working properly')
        
    def testSetServiceRequestFirstReturnValue(self):
        s = st.Status(address = 6)
        self.assertEqual(s.setServiceRequest(), False, 'setServiceRequest not working properly')
        
    def testSetServiceRequestFirstStatusChange(self):
        s = st.Status(address = 6)
        s.setServiceRequest()
        self.assertEqual(s.requestService, True, 'setServiceRequest not working properly')
        
    def testIsServiceRequestedSRTrue(self):
        s = st.Status(address = 11)
        s.setServiceRequest()
        self.assertEqual(s.isServiceRequested(), True, 'isServiceRequested not working properly')
        
    def testIsServiceRequestedSNRFalse(self):
        s = st.Status(address = 11)
        self.assertEqual(s.isServiceRequested(), False, 'isServiceRequested not working properly')
        
    def testSetMessageErrorRepeatReturnValue(self):
        s = st.Status(address = 24)
        s.setMessageError()
        self.assertEqual(s.setMessageError(), True, 'setMessageError not working properly')
        
    def testSetMessageErrorRepeatStatusChange(self):
        s = st.Status(address = 24)
        s.setMessageError()
        s.setMessageError()
        self.assertEqual(s.messageError, True, 'setMessageError not working properly')
        
    def testSetMessageErrorFirstReturnValue(self):
        s = st.Status(address = 24)
        self.assertEqual(s.setMessageError(), False, 'setMessageError not working properly')
        
    def testSetMessageErrorFirstStatusChange(self):    
        s = st.Status(address = 24)
        s.setMessageError()
        self.assertEqual(s.messageError, True, 'setMessageError not working properly')
         
    def testIsMessageErrorTrue(self):
        s = st.Status(address = 24)
        s.setMessageError()
        self.assertEqual(s.isMessageError(), True, 'setMessageError not working properly')
        
    def testIsMessageErrorFalse(self):
        s = st.Status(address = 24)
        self.assertEqual(s.isMessageError(), False, 'setMessageError not working properly')
        
    def testSetBusyRepeatReturnValue(self):
        s = st.Status(address = 24)
        s.setBusy()
        self.assertEqual(s.setBusy(), True, 'setBusy not working properly')
        
    def testSetBusyRepeatStatusChange(self):
        s = st.Status(address = 24)
        s.setBusy()
        s.setBusy()
        self.assertEqual(s.busy, True, 'setBusy not working properly')
        
    def testSetBusyFirstReturnValue(self):
        s = st.Status(address = 24)
        self.assertEqual(s.setBusy(), False, 'setBusy not working properly')
        
    def testSetBusyFirstStatusChange(self):
        s = st.Status(address = 24)
        s.setBusy()
        self.assertEqual(s.busy, True, 'setBusy not working properly')
             
    def testIsBusyTrue(self):
        s = st.Status(address = 24)
        s.setBusy()
        self.assertEqual(s.isBusy(), True, 'setBusy not working properly')
        
    def testIsBusyFalse(self): 
        s = st.Status(address = 24)
        self.assertEqual(s.isBusy(), False, 'setBusy not working properly')
#     