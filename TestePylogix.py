"""
Reading a UDT will return the raw byte data, it is up to you as the user
to understand how it is packed and how to unpack it.  Looking at the data
type in L5K format can be helpful.

This example is reading the entire structure of a timer in 1 read.
For a timer, bytes 2-5 contain the .EN, .TT packed at the end of the word.
Bytes 6-9 contain the preset and bytes 10-13 contain the acc value
"""
from pylogix import PLC
from struct import pack, unpack_from


class Timer(object):
    
    def __init__(self, data):
        
        self.PRE = unpack_from('<i', data, 4)[0]
        self.ACC = unpack_from('<i', data, 8)[0]
        bits = unpack_from('<i', data, 0)[0]
        self.EN = get_bit(bits, 31)
        self.TT = get_bit(bits, 30)
        self.DN = get_bit(bits, 29)
class Couter(object):
    
    def __init__(self, data):
        
        self.PRE = unpack_from('<i', data, 4)[0]
        self.ACC = unpack_from('<i', data, 8)[0]
        bits = unpack_from('<i', data, 0)[0]
        self.CU = get_bit(bits, 31)
        self.CD = get_bit(bits, 30)
        self.DN = get_bit(bits, 29)
        self.OV = get_bit(bits, 28)
        self.UN = get_bit(bits, 27)

def get_bit(value, bit_number):
    """
    Returns the specific bit of a word
    """
    mask = 1 << bit_number
    if value & mask:
        return True
    else:
        return False


with PLC() as comm:
    comm.IPAddress = '172.16.0.110'
    ret = comm.Read('AXIS01.ActualPosition')
    #C = Couter(ret.Value)
    #print(C.PRE, C.ACC, C.CU, C.CD, C.DN, C.OV, C.UN)
    print(ret.Status)
    print(ret.Value)


