# -*- coding: utf-8 -*-
import hashlib
import HashingLibrary
from bitstring import BitArray, BitStream

def computeHammingDistance( simhash1, simhash2 ):
    h1 = BitArray( simhash1 )
    h2 = BitArray( simhash2 )
    return ( h1^h2  ).count( True );

class SimHash:
    def __init__( self ):
        self.num_bits = 64
        self.simhash_array = [ 0.0 for i in range( self.num_bits ) ]
        self.hash_function = hashlib.md5()
        
    def updateHash( self, token, weight ):
        hl = HashingLibrary.HashingLibrary()
        hl.updateHash( token )
        hl_hex_digest = hl.getHexDigest()
        hl_bit_string = hl.getBinaryString()
        i = 0
        while ( i < self.num_bits ):
            if int( hl_bit_string[i] ) == 0:
                self.simhash_array[i] = self.simhash_array[i] - weight
            else:
                self.simhash_array[i] = self.simhash_array[i] + weight
            i = i + 1
        return;
    
    def getSimHash( self ):
        bit_string = ''
        for i in range( self.num_bits ):
            if self.simhash_array[i] <= 0:
                bit_string = bit_string+'0'
            else:
                bit_string = bit_string+'1'
        hex_hash = hex( int( bit_string, 2 ) )
        hex_hash_string = str( hex_hash[0:18] )
        return hex_hash_string;
        
    
