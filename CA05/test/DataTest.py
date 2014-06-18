'''
Created on Apr 1, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Data as data

class Test(unittest.TestCase):
    def testInitExists(self):
        d = data.Data(payload = 0)
        assert "__init__" in dir(d), 'Method by name __init__ does not exists'
    
    def testSetContentExists(self):
        d = data.Data(payload = 0)
        assert "setContent" in dir(d), 'Method by name setContent does not exists'
        
    def testIsPayloadValidExists(self):
        d = data.Data(payload = 0)
        assert "isPayloadValid" in dir(d), 'Method by name isPayloadValid does not exists'
        
    def testgetContentExists(self):
        d = data.Data(payload = 0)
        assert "getContent" in dir(d), 'Method by name getContent does not exists'
    
    def testDWInstantiationWithValidLForReturnType(self):
        d = data.Data(payload = 0)
        assert isinstance(d, data.Data), 'data is not an instance of Data'
        
    def testDWInstantiationWithValidLForPayload(self):
        d = data.Data(payload = 0)
        self.assertEqual(d.payload, 0 , 'Data constructor does not work properly')
        
    def testDWInstantiationWithNoParamForReturnType(self):
        d = data.Data()
        assert isinstance(d, data.Data), 'data is not an instance of Data'        
        
    def testDWInstantiationWithNoParamForPayload(self):
        d = data.Data()
        self.assertEqual(d.payload, 0 , 'Data constructor does not work properly')

    def testDWInstantiationWithValidHForReturnType(self):
        d = data.Data(payload = 65535)
        assert isinstance(d, data.Data), 'data is not an instance of Data'        
        
    def testDWInstantiationWithValidHForPayload(self):
        d = data.Data(payload = 65535)
        self.assertEqual(d.payload, 65535 , 'Data constructor does not work properly')
        
    def testDWInstantiationWithAlphaNumericForErrorType(self):
        self.assertRaises(ValueError, data.Data, ('a'))        
        
    def testDWInstantiationWithAlphaNumericForErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Data.__init__:\s\s", data.Data, ('a'))      
        
    def testDWInstantiationWithNegativeForErrorType(self):
        self.assertRaises(ValueError, data.Data, (-2))        
        
    def testDWInstantiationWithNegativeForErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Data.__init__:\s\s", data.Data, (-2)) 
        
    def testDWInstantiationWithValidForReturnType(self):
        d = data.Data(payload = 1)
        assert isinstance(d, data.Data), 'data is not an instance of Data'        
        
    def testDWInstantiationWithValidForPayload(self):
        d = data.Data(payload = 1)
        self.assertEqual(d.payload, 1 , 'Data constructor does not work properly')
        
    def testDWInstantiationWithInvalidHForErrorType(self):
        self.assertRaises(ValueError, data.Data, (65536))        
        
    def testDWInstantiationWithInvalidHForErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Data.__init__:\s\s", data.Data, (65536)) 
        
    def testSetContentWithValidForReturnValue(self):
        d = data.Data()
        d.setContent(payload = 1)
        self.assertEqual(d.payload, 1 , 'Set content does not work properly')
        
    def testSetContentWithValidForPayload(self):
        d = data.Data()
        self.assertEqual(d.setContent(payload = 1), 1 , 'Set content does not work properly')
        
    def testSetContentWithNoParamForErrorType(self):
        d = data.Data()
        self.assertRaises(ValueError, d.setContent)
        
    def testSetContentWithNoParamForErrorMessage(self):
        d = data.Data()
        self.assertRaisesRegexp(Exception, "^Data.setContent:\s\s", d.setContent)
        
    def testSetContentWithValidHForReturnValue(self):
        d = data.Data()
        d.setContent(payload = 65535)
        self.assertEqual(d.payload, 65535 , 'Set content does not work properly')     
        
    def testSetContentWithValidHForPayload(self):
        d = data.Data()
        self.assertEqual(d.setContent(payload = 65535), 65535 , 'Set content does not work properly')
        
    def testSetContentWithAlphaNumericForErrorType(self):
        d = data.Data()
        self.assertRaises(ValueError, d.setContent, ('a'))
        
    def testSetContentWithAlphaNumericForErrorMessage(self):
        d = data.Data()
        self.assertRaisesRegexp(Exception, "^Data.setContent:\s\s", d.setContent, ('a'))
        
    def testSetContentWithNegativeForErrorType(self):
        d = data.Data()
        self.assertRaises(ValueError, d.setContent, (-2))
        
    def testSetContentWithNegativeForErrorMessage(self):
        d = data.Data()
        self.assertRaisesRegexp(Exception, "^Data.setContent:\s\s", d.setContent, (-2))
        
    def testSetContentWithInvalidHForErrorType(self):
        d = data.Data()
        self.assertRaises(ValueError, d.setContent, (65536))
        
    def testSetContentWithInvalidHForErrorMessage(self):
        d = data.Data()
        self.assertRaisesRegexp(Exception, "^Data.setContent:\s\s", d.setContent, (65536)) 
        
    def testGetContent(self):
        d = data.Data()
        self.assertEqual(d.getContent(), d.payload, 'Get content is not working properly')
        
    def testIsPayloadValidWithValid(self):
        d = data.Data()
        self.assertEqual(d.isPayloadValid(payload = 1), True , 'isPayloadValid does not work properly')
            
    def testIsPayloadValidWithValidHForReturnType(self):
        d = data.Data()
        self.assertEqual(d.isPayloadValid(payload = 65535), True , 'isPayloadValid does not work properly')     
        
    def testIsPayloadValidWithAlphaNumericForErrorType(self):
        d = data.Data()
        self.assertEqual(d.isPayloadValid(payload = 'a'), False , 'isPayloadValid does not work properly') 
    
    def testIsPayloadValidWithNegative(self):
        d = data.Data()
        self.assertEqual(d.isPayloadValid(payload = -2), False , 'isPayloadValid does not work properly')
        
    def testIsPayloadValidWithInvalidH(self):
        d = data.Data()
        self.assertEqual(d.isPayloadValid(payload = 65536), False , 'isPayloadValid does not work properly')
        