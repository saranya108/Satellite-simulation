'''
Created on Apr 1, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Word as wrd

class Test(unittest.TestCase):        
    def testInitExists(self):
        w = wrd.Word(address = 2)
        assert "__init__" in dir(w), 'Method by name __init__ does not exists'
        
    def testgetTerminalAddressExists(self):
        w = wrd.Word(address = 2)
        assert "getTerminalAddress" in dir(w), 'Method by name getTerminalAddress does not exists' 
          
    def testWordInstantiationWithValidLForReturnType(self):
        w = wrd.Word(address = 2)
        assert isinstance(w, wrd.Word), 'Word constructor does not return Word instance'
        
    def testWordInstantiationWithValidLForAdd(self):
        w = wrd.Word(address = 2)
        self.assertEqual(w.address, 2, 'Word constructor does not store address') 

    def testWordInstantiationWithZeroErrorType(self):
        self.assertRaises(ValueError, wrd.Word, (0))
      
    def testWordInstantiationWithZeroErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Word.__init__:\s\s", wrd.Word, (0))
        
    def testWordInstantiationWithAlphaNumericErrorType(self):
        self.assertRaises(ValueError, wrd.Word, ('a'))
      
    def testWordInstantiationWithAlphaNumericErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Word.__init__:\s\s", wrd.Word, ('a'))
    
    def testWordInstantiationWithNegativeErrorType(self):
        self.assertRaises(ValueError, wrd.Word, (-1))
      
    def testWordInstantiationWithNegativeErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Word.__init__:\s\s", wrd.Word, (-1))    
    
    def testWordInstantiationWithInvalidHB1ErrorType(self):
        self.assertRaises(ValueError, wrd.Word, (31))
      
    def testWordInstantiationWithInvalidHB1ErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Word.__init__:\s\s", wrd.Word, (31))
        
    def testWordInstantiationWithInvalidHB2ErrorType(self):
        self.assertRaises(ValueError, wrd.Word, (32))
      
    def testWordInstantiationWithInvalidHB2ErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Word.__init__:\s\s", wrd.Word, (32))
    
    def testWordInstantiationWithValidHReturnType(self):
        w = wrd.Word(address = 30)
        assert isinstance(w, wrd.Word), 'Word constructor does not return Word instance'
      
    def testWordInstantiationWithValidHForAdd(self):
        w = wrd.Word(address = 30)
        self.assertEqual(w.address, 30, 'Word constructor does not store address')  
        
    def testGetTerminalAddressForReturnType(self):
        w = wrd.Word(address = 4)
        assert isinstance(w.getTerminalAddress(), int), 'Terminal address of word not an integer'
        
    def testGetTerminalAddressForReturnValue(self):
        w=wrd.Word(address = 4)
        self.assertEqual(w.getTerminalAddress(), 4, 'Terminal address of word not of correct value')
        
    