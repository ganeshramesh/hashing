# -*- coding: utf-8 -*-
import hashlib
import binascii

def byte_to_binary( n ):
    return ''.join( str( ( n & ( 1 << i ) ) and 1 ) for i in reversed( range( 8 ) ) )

def hex_to_binary( h ):
    return ''.join( byte_to_binary( ord( b ) ) for b in binascii.unhexlify( h ) )

def get_binary_value( s ):
    if s == '0':
        ret_string = '0000'
    elif s == '1':
        ret_string = '0001'
    elif s == '2':
        ret_string = '0010'
    elif s == '3':
        ret_string = '0011'
    elif s == '4':
        ret_string = '0100'
    elif s == '5':
        ret_string = '0101'
    elif s == '6':
        ret_string = '0110'
    elif s == '7':
        ret_string = '0111'
    elif s == '8':
        ret_string = '1000'
    elif s == '9':
        ret_string = '1001'
    elif s == 'a':
        ret_string = '1010'
    elif s == 'b':
        ret_string = '1011'
    elif s == 'c':
        ret_string = '1100'
    elif s == 'd':
        ret_string = '1101'
    elif s == 'e':
        ret_string = '1110'
    elif s == 'f':
        ret_string = '1111'
    return ret_string;
    
class HashingLibrary:

    def __init__( self,hash_type='md5',numbits=64 ):
        self.hash_function = hashlib.md5()
        
    def updateHash( self, keyword_string ):
        self.hash_function.update( keyword_string )
        return;
        
    def getHexDigest( self ):
        return self.hash_function.hexdigest();

    def getBinaryString( self ):
        hex_string = self.hash_function.hexdigest()
        print len( hex_string )
        list_of_binaries = [] 
        for i in range( len( hex_string ) ):            
            list_of_binaries.append( get_binary_value( hex_string[i] ) )
        return ''.join( list_of_binaries );
        