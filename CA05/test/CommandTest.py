'''
Created on Apr 4, 2014

@author: Saranya Sadasivam
'''
import unittest
import CA05.prod.Command as com

class Test(unittest.TestCase):
    def testInitExists(self):
        c = com.Command(address = 2)
        assert "__init__" in dir(c), 'Method by name __init__ does not exists'
    
    def testGetTerminalAddressExists(self):
        c = com.Command(address = 2)
        assert "getTerminalAddress" in dir(c), 'Method by name getTerminalAddress does not exists'
        
    def testSetToCommandWordExists(self):
        c = com.Command(address = 2)
        assert "setToCommandWord" in dir(c), 'Method by name setToCommandWord does not exists'
        
    def testSetToModeCommandExists(self):
        c = com.Command(address = 2)
        assert "setToModeCommand" in dir(c), 'Method by name setToModeCommand does not exists'
        
    def testGetModeCodeExists(self):
        c = com.Command(address = 2)
        assert "getModeCode" in dir(c), 'Method by name getModeCode does not exists'
        
    def testIsModeCommandExists(self):
        c = com.Command(address = 2)
        assert "isModeCommand" in dir(c), 'Method by name isModeCommand does not exists'
        
    def testSetSubAddressExists(self):
        c = com.Command(address = 2)
        assert "setSubAddress" in dir(c), 'Method by name setSubAddress does not exists'
        
    def testGetSubAddressExists(self):
        c = com.Command(address = 2)
        assert "getSubAddress" in dir(c), 'Method by name getSubAddress does not exists'
        
    def testSetWordCountExists(self):
        c = com.Command(address = 2)
        assert "setWordCount" in dir(c), 'Method by name setWordCount does not exists'
        
    def testGetWordCountExists(self):
        c = com.Command(address = 2)
        assert "getWordCount" in dir(c), 'Method by name getWordCount does not exists'
        
    def testSetTransmitCommandExists(self):
        c = com.Command(address = 2)
        assert "setTransmitCommand" in dir(c), 'Method by name setTransmitCommand does not exists'
        
    def testSetReceiveCommandExists(self):
        c = com.Command(address = 2)
        assert "setReceiveCommand" in dir(c), 'Method by name setReceiveCommand does not exists'
        
    def testIsTransmitCommandExists(self):
        c = com.Command(address = 2)
        assert "isTransmitCommand" in dir(c), 'Method by name isTransmitCommand does not exists'
        
    def testCWInstantiationValidReturnType(self):
        c = com.Command(address = 2)
        assert isinstance(c, com.Command),'Command is not instantiated properly'
        
    def testCWInstantiationValidAddress(self):
        c = com.Command(address = 2)
        self.assertEqual(c.address, 2, 'Command is not instantiated properly')

    def testCWInstantiationValidModeCommand(self):
        c = com.Command(address = 2)
        self.assertEqual(c.modeCommand, True, 'Command is not instantiated properly')
        
    def testCWInstantiationValidTR(self):
        c = com.Command(address = 2)
        self.assertEqual(c.tr, False, 'Command is not instantiated properly')
        
    def testCWInstantiationValidModeCode(self):
        c = com.Command(address = 2)
        self.assertEqual(c.modeCode, c.transmitStatusWord, 'Command is not instantiated properly')
        
    def testCWInstantiationNoParamErrorType(self):
        self.assertRaises(ValueError, com.Command,(None))
        
    def testCWInstantiationNoParamErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(None))
        
    def testCWInstantiationAlphaNumericErrorType(self):
        self.assertRaises(ValueError, com.Command,('a'))
        
    def testCWInstantiationAlphaNumericErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,('a'))
        
    def testCWInstantiationNegativeErrorType(self):
        self.assertRaises(ValueError, com.Command,(-1))
        
    def testCWInstantiationNegativeErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(-1))
                
    def testCWInstantiationInvalidLErrorType(self):
        self.assertRaises(ValueError, com.Command,(0))
        
    def testCWInstantiationInvalidLErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(0))
        
    def testCWInstantiationValidLReturnType(self):
        c = com.Command(address = 1)
        assert isinstance(c, com.Command),'Command is not instantiated properly'
        
    def testCWInstantiationValidLAddress(self):
        c = com.Command(address = 1)
        self.assertEqual(c.address, 1, 'Command is not instantiated properly')
        
    def testCWInstantiationValidLModeCommand(self):
        c = com.Command(address = 1)
        self.assertEqual(c.modeCommand, True, 'Command is not instantiated properly')
        
    def testCWInstantiationValidLTR(self):
        c = com.Command(address = 1)
        self.assertEqual(c.tr, False, 'Command is not instantiated properly')
        
    def testCWInstantiationValidLModeCode(self):
        c = com.Command(address = 1)
        self.assertEqual(c.modeCode, c.transmitStatusWord, 'Command is not instantiated properly')
        
    def testCWInstantiationFloatErrorType(self):
        self.assertRaises(ValueError, com.Command,(1.2))
        
    def testCWInstantiationFloatErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(1.2))
        
    def testCWInstantiationValidHReturnType(self):
        c = com.Command(address = 30)
        assert isinstance(c, com.Command),'Command is not instantiated properly'
        
    def testCWInstantiationValidHAddress(self):
        c = com.Command(address = 30)
        self.assertEqual(c.address, 30, 'Command is not instantiated properly')
        
    def testCWInstantiationValidHModeCommand(self):
        c = com.Command(address = 30)
        self.assertEqual(c.modeCommand, True, 'Command is not instantiated properly')
        
    def testCWInstantiationValidHTR(self):
        c = com.Command(address = 30)
        self.assertEqual(c.tr, False, 'Command is not instantiated properly')
        
    def testCWInstantiationValidHModeCode(self):
        c = com.Command(address = 30)
        self.assertEqual(c.modeCode, c.transmitStatusWord, 'Command is not instantiated properly')
        
    def testCWInstantiationInvalidErrorType(self):
        self.assertRaises(ValueError, com.Command,(31))
        
    def testCWInstantiationInvalidErrorMessage(self):
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(31))
        
    def testCWInstantiationInvalidHErrorType(self):
        self.assertRaises(ValueError, com.Command,(32))
        
    def testCWInstantiationInvalidHErrorMessage(self):  
        self.assertRaisesRegexp(Exception, "^Command.__init__:\s\s", com.Command,(32))
        
    def testGetTerminalAddressForReturnType(self):
        c = com.Command(address = 6)
        assert isinstance(c, com.Command),'getTerminalAddress is not working properly'
        
    def testGetTerminalAddressForReturnValue(self):
        c = com.Command(address = 6)
        self.assertEqual(c.getTerminalAddress(), 6, 'getTerminalAddress is not working properly')
        
    def testSetToCommandWordCWReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 23)
        self.assertEqual(c.setToCommandWord(address = 23), True, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWWordCount(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 23)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWSubAddress(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 23)
        self.assertEqual(c.subAddress, 23, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        self.assertEqual(c.setToCommandWord(address = 23), False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWStateChange(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 23)
        self.assertEqual(c.modeCommand, False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWWordCount(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 23)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 23)
        self.assertEqual(c.subAddress, 23, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWNoParamReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord()
        self.assertEqual(c.setToCommandWord(), True, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWNoParamWordCount(self):
        c = com.Command(address = 2)
        c.setToCommandWord()
        c.setToCommandWord()
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWNoParamSubAddress(self):
        c = com.Command(address = 2)
        c.setToCommandWord()
        c.setToCommandWord()
        self.assertEqual(c.subAddress, 1, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWNoParamReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord()
        self.assertEqual(c.setToCommandWord(), True, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWNoParamStateChange(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord()
        self.assertEqual(c.modeCommand, False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWNoParamWordCount(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord()
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWNoParamSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord()
        self.assertEqual(c.subAddress, 1, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWAlphaNumericErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,('a'))
        
    def testSetToCommandWordCWAlphaNumericErrorMessage(self):   
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,('a'))
        
    def testSetToCommandWordCWNegativeErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,(-1))
        
    def testSetToCommandWordCWNegativeErrorMessage(self): 
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,(-1))
        
    def testSetToCommandWordCWInvalidLErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,(0))
        
    def testSetToCommandWordCWInvalidLErrorMessage(self): 
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,(0))
            
    def testSetToCommandWordCWValidLReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(1)
        self.assertEqual(c.setToCommandWord(address = 1), True, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWValidLWordCount(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 1)
        c.setToCommandWord(address = 1)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWValidLSubAddress(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 1)
        c.setToCommandWord(address = 1)
        self.assertEqual(c.subAddress, 1, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidLReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        self.assertEqual(c.setToCommandWord(address = 1), False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidLStateChange(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 1)
        self.assertEqual(c.modeCommand, False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidLWordCount(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(1)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidLSubAddress(self):   
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 1)
        self.assertEqual(c.subAddress, 1, 'setToCommandWord is not working properly')
         
    def testSetToCommandWordCWDecimalErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,(1.2))
        
    def testSetToCommandWordCWDecimalErrorMessage(self):   
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,(1.2))
        
    def testSetToCommandWordCWValidHReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 30)
        self.assertEqual(c.setToCommandWord(address = 30), True, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWValidHWordCount(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 30)
        c.setToCommandWord(address = 30)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWValidHSubAddress(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 30)
        c.setToCommandWord(address = 30)
        self.assertEqual(c.subAddress, 30, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidHReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        self.assertEqual(c.setToCommandWord(address = 30), False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidHStateChange(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 30)
        self.assertEqual(c.modeCommand, False, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidHWordCount(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 30)
        self.assertEqual(c.wordCount, 0, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordNCWValidHSubAddress(self):    
        c = com.Command(address = 2)
        c.setToModeCommand()
        c.setToCommandWord(address = 30)
        self.assertEqual(c.subAddress, 30, 'setToCommandWord is not working properly')
        
    def testSetToCommandWordCWInvalidHErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,(31))
        
    def testSetToCommandWordCWInvalidHErrorMessage(self):
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,(31))     
        
    def testSetToCommandWordCWInvalidErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToCommandWord,(32))
        
    def testSetToCommandWordCWInvalidErrorMessage(self): 
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToCommandWord:\s\s", c.setToCommandWord ,(32))
        
    def testSetToModeCommandNoParamForReturnValue(self):   
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(), c.transmitStatusWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandNoParamForModeCode(self):
        c = com.Command(address = 2)
        c.setToModeCommand()
        self.assertEqual(c.modeCode, c.transmitStatusWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandNoParamForSubAddress(self): 
        c = com.Command(address = 2)
        c.setToModeCommand()
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTSWForReturnValue(self): 
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(mode = c.transmitStatusWord), c.transmitStatusWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTSWForModeCode(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertEqual(c.modeCode, c.transmitStatusWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTSWForSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand(c.transmitStatusWord)
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandSDForReturnValue(self):  
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(mode = c.shutDown), c.shutDown, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandSDForModeCode(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.shutDown)
        self.assertEqual(c.modeCode, c.shutDown, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandSDForSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.shutDown)
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandRForReturnValue(self):
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(mode = c.reset), c.reset, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandRForModeCode(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.reset)
        self.assertEqual(c.modeCode, c.reset, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandRForSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.reset)
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTVWForReturnValue(self):   
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(mode = c.transmitVectorWord), c.transmitVectorWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTVWForModeCode(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitVectorWord)
        self.assertEqual(c.modeCode, c.transmitVectorWord, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTVWForSubAddress(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitVectorWord)
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTLCForReturnValue(self):   
        c = com.Command(address = 2)
        self.assertEqual(c.setToModeCommand(mode = c.transmitLastCommand), c.transmitLastCommand, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTLCForModeCode(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitLastCommand)
        self.assertEqual(c.modeCode, c.transmitLastCommand, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandTLCForSubAddress(self):      
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitLastCommand)
        self.assertEqual(c.subAddress, 0, 'setToModeCommand is not working properly')
        
    def testSetToModeCommandAlphaNumericErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToModeCommand,('a'))
        
    def testSetToModeCommandAlphaNumericErrorMessage(self):
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToModeCommand:\s\s", c.setToModeCommand ,('a'))
         
    def testSetToModeCommandInvalidNumberErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToModeCommand,(5))
        
    def testSetToModeCommandInvalidNumberErrorMessage(self): 
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToModeCommand:\s\s", c.setToModeCommand ,(5))
           
    def testSetToModeCommandNegativeErrorType(self):
        c = com.Command(address = 2)
        self.assertRaises(ValueError, c.setToModeCommand,(-1))
        
    def testSetToModeCommandNegativeErrorMessage(self):
        c = com.Command(address = 2)
        self.assertRaisesRegexp(Exception, "^Command.setToModeCommand:\s\s", c.setToModeCommand ,(-1))
        
    def testGetModeCodeMCReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.shutDown)
        self.assertEqual(c.getModeCode() ,c.shutDown, 'getModeCode is not working properly')
        
    def testGetModeCodeNMCErrorType(self):    
        c = com.Command(address = 2)
        c.setToCommandWord(address = 22)
        self.assertRaises(ValueError, c.getModeCode)
        
    def testGetModeCodeNMCErrorMessage(self):    
        c = com.Command(address = 2)
        c.setToCommandWord(address = 22)
        self.assertRaisesRegexp(Exception, "^Command.getModeCode:\s\s", c.getModeCode)
        
    def testIsModeCommandMCReturnValue(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.shutDown)
        self.assertEqual(c.isModeCommand() ,True , 'isModeCommand is not working properly')
        
    def testIsModeCommandNMCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 22)
        self.assertEqual(c.isModeCommand() ,False , 'isModeCommand is not working properly')
        
    def testSetSubAddressValidReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 2)
        self.assertEqual(c.setSubAddress(address = 2) ,2 , 'setSubAddress is not working properly')
        
    def testSetSubAddressNCWValidStatusChange(self):   
        c = com.Command(address = 2)
        c.setToCommandWord(address = 2)
        c.setSubAddress(address = 2)
        self.assertEqual(c.subAddress,2 , 'setSubAddress is not working properly')
        
    def testSetSubAddressMCNoParamErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, ())
        
    def testSetSubAddressMCNoParamErrorMessage(self):   
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,())
        
    def testSetSubAddressMCAlphaNumericErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, ('a'))
        
    def testSetSubAddressMCAlphaNumericErrorMessage(self):  
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,('a')) 
        
    def testSetSubAddressMCNegativeErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (-1))
        
    def testSetSubAddressMCNegativeErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(-1))
        
    def testSetSubAddressMCInvalidLErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (0))
        
    def testSetSubAddressMCInvalidLErrorMessage(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(0))
        
    def testSetSubAddressNMCValidLReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        self.assertEqual(c.setSubAddress(address = 1) ,1 , 'setSubAddress is not working properly')
        
    def testSetSubAddressNMCValidLStatusChange(self):   
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setSubAddress(address = 1)
        self.assertEqual(c.subAddress, 1, 'setSubAddress is not working properly')
        
    def testSetSubAddressMCDecimalErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (1.2))
        
    def testSetSubAddressMCDecimalErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(1.2))
        
    def testSetSubAddressNMCValidHReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        self.assertEqual(c.setSubAddress(address = 30) ,30 , 'setSubAddress is not working properly')
        
    def testSetSubAddressNMCValidHStatusChange(self):    
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setSubAddress(address = 30)
        self.assertEqual(c.subAddress, 30, 'setSubAddress is not working properly')
        
    def testSetSubAddressMCInvalidHErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (31))
        
    def testSetSubAddressMCInvalidHErrorMessage(self):   
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(31))
        
    def testSetSubAddressMCInvalidErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (32))
        
    def testSetSubAddressMCInvalidErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(32))
        
    def testSetSubAddressNCWErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setSubAddress, (4))
        
    def testSetSubAddressNCWErrorMessage(self):  
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setSubAddress:\s\s", c.setSubAddress ,(4))
            
    def testGetSubAddressNMCReturnType(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 2)
        c.setSubAddress(address = 4)
        assert isinstance(c.getSubAddress(), int), 'getSubAddress not working properly'
        
    def testGetSubAddressNMCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 2)
        c.setSubAddress(address = 4)
        self.assertEqual(c.getSubAddress(), 4, 'getSubAddress not working properly')
        
    def testGetSubAddressMCErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.getSubAddress)
        
    def testGetSubAddressMCErrorMessage(self):   
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.getSubAddress:\s\s", c.getSubAddress)
         
    def testSetWordCountMCValidReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        self.assertEqual(c.setWordCount(count = 2), 2, 'setWordCount not working properly')
        
    def testSetWordCountCWValidStateChange(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        c.setWordCount(count = 2)
        self.assertEqual(c.wordCount, 2, 'setWordCount not working properly')
        
    def testSetWordCountCWNoParamErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount)
        
    def testSetWordCountCWNoParamErrorMessage(self):   
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount)
         
    def testSetWordCountCWAlphaNumericErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, ('a'))
        
    def testSetWordCountCWAlphaNumericErrorMessage(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, ('a'))
             
    def testSetWordCountCWNegativeErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, (-1))
        
    def testSetWordCountCWNegativeErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, (-1))
        
    def testSetWordCountCWInvalidLErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, (0))
        
    def testSetWordCountCWInvalidLErrorMessage(self): 
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, (0))
        
    def testSetWordCountCWValidLReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        self.assertEqual(c.setWordCount(count = 1), 1, 'setWordCount not working properly')
        
    def testSetWordCountCWValidLStatusChange(self):   
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        c.setWordCount(count = 1)
        self.assertEqual(c.wordCount, 1, 'setWordCount not working properly')
                         
    def testSetWordCountCWDecimalErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, (1.2))
        
    def testSetWordCountCWDecimalErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, (1.2))
        
    def testSetWordCountCWValidHReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        self.assertEqual(c.setWordCount(count = 30), 30, 'setWordCount not working properly')
        
    def testSetWordCountCWValidHStatusChange(self):    
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        c.setWordCount(count = 30)
        self.assertEqual(c.wordCount, 30, 'setWordCount not working properly')
        
    def testSetWordCountCWInvalidHErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, (31))
        
    def testSetWordCountCWInvalidHErrorMessage(self):   
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, (31))
        
    def testSetWordCountCWInvalidErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaises(ValueError, c.setWordCount, (32))
        
    def testSetWordCountCWInvalidErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = c.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount, (32))
        
    def testSetWordCountNCWErrorType(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        self.assertRaises(ValueError, c.setWordCount,())
        
    def testSetWordCountNCWErrorMessage(self):         
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        self.assertRaisesRegexp(Exception, "^Command.setWordCount:\s\s", c.setWordCount)
        
    def testGetWordCountCWReturnType(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        c.setWordCount(count = 4)
        assert isinstance(c.getWordCount(), int),'getWordCount not working properly'
        
    def testGetWordCountCWReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 5)
        c.setWordCount(count = 4)
        self.assertEqual(c.getWordCount(), 4, 'getWordCount not working properly')
        
    def testGetWordCountNMCErrorType(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = com.Command.transmitStatusWord)
        self.assertRaises(ValueError, c.getWordCount)
         
    def testGetWordCountNCWErrorMessage(self):
        c = com.Command(address = 2)
        c.setToModeCommand(mode = com.Command.transmitStatusWord)
        self.assertRaisesRegexp(Exception, "^Command.getWordCount:\s\s", c.getWordCount)
         
    def testSetTransmitCommandTCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setTransmitCommand()
        self.assertEqual(c.setTransmitCommand(), True, 'setTransmitCommand not working properly')
        
    def testSetTransmitCommandTCTR(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setTransmitCommand()
        c.setTransmitCommand()
        self.assertEqual(c.tr, True, 'setTransmitCommand not working properly')
        
    def testSetTransmitCommandRCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setReceiveCommand()
        self.assertEqual(c.setTransmitCommand(), False, 'setTransmitCommand not working properly')
        
    def testSetTransmitCommandRCTR(self):   
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setReceiveCommand()
        c.setTransmitCommand()
        self.assertEqual(c.tr, True, 'setTransmitCommand not working properly')
        
    def testSetReceiveCommandRCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setReceiveCommand()
        self.assertEqual(c.setReceiveCommand(), True, 'setReceiveCommand not working properly')
        
    def testSetReceiveCommandRCTR(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setReceiveCommand()
        c.setReceiveCommand()
        self.assertEqual(c.tr, False, 'setReceiveCommand not working properly')
        
    def testSetReceiveCommandTCReturnValue(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setTransmitCommand()
        self.assertEqual(c.setReceiveCommand(), False, 'setReceiveCommand not working properly')
        
    def testSetReceiveCommandTCTR(self):   
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setTransmitCommand()
        c.setReceiveCommand()
        self.assertEqual(c.tr, False, 'setReceiveCommand not working properly')
        
    def testIsTransmitCommandTC(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setTransmitCommand()
        self.assertEqual(c.isTransmitCommand(), True, 'isTransmitCommand not working properly')
        
    def testIsTransmitCommandRC(self):
        c = com.Command(address = 2)
        c.setToCommandWord(address = 3)
        c.setReceiveCommand()
        self.assertEqual(c.isTransmitCommand(), False, 'isTransmitCommand not working properly')
        
#         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            