'''Autogenerated dummy lx package enabling code completion in Python editors
 MODO Build #100509
'''

import ifc
import object
import result
import service
import symbol



class Monitor:
    def init(self):
        '''Initialize the monitor with the total number of steps'''
        pass

    def step(self):
        '''Increment the monitor by one or by step it by an arbitrary amount'''
        pass



class Service:
    def name(self):
        '''Return the name of the script service.'''
        pass

    def query(self):
        '''Query an attribute from the selection.'''
        pass

    def query1(self):
        '''Query an attribute from the selection, returning a single value.'''
        pass

    def queryN(self):
        '''Query an attribute from the selection, returning a tuple.'''
        pass

    def select(self, element):
        '''Select a an attribute (and element) for query.'''
        pass



def arg():
    '''Get the argument string for the script.'''
    pass

def args():
    '''Get the parsed argument tuple for the script.'''
    pass

def bless():
    '''Amen.'''
    pass

def command():
    '''Execute a command with a variable argument list.'''
    pass

def eval():
    '''Evaluate a command string.'''
    pass

def eval1():
    '''Evaluate a command string, returning a single value.'''
    pass

def evalN():
    '''Evaluate a command string, returning a tuple.'''
    pass

def extract():
    '''Extract the Python object referenced from a COM object wrapper.'''
    pass

def getQWidget():
    '''Converts a PyLong object to a PySide QWidget'''
    pass

def lastResult():
    '''Get the result code from the last service or object method called.'''
    pass

def notimpl():
    '''Raise 'not implemented' exception.'''
    pass

def option():
    '''Get the current state of an option'''
    pass

def out():
    '''Output to log.'''
    pass

def outEx():
    '''Output the exception state to the log.'''
    pass

def queryToggle():
    '''Query a command with a ToggleValue style argument.'''
    pass

def setOption():
    '''Set options that affect how the lx methods act'''
    pass

def test():
    '''Test the state of a toggle argument.'''
    pass

def throw():
    '''Raise a result code exception.'''
    pass

def trace():
    '''Toggle extra Event Log output for each lx function call.'''
    pass

