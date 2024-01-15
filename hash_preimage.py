import binascii
import hashlib
import os
import string
import random
import binascii

def DecToBinary(num):
    #return bin(num).replace("0b", "")
    return bin(num)[2:].zfill(256)

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    #nonce = b'\x00'
    finding = -1
    while finding < 0:
        rand1 = random.randrange(1, 100, 2)
        letters = string.ascii_letters
        x = ''.join(random.choices(string.ascii_letters, k=rand1))
        #print(x)

        str_SHX = hashlib.sha256(x.encode('utf-8')).hexdigest()
        #print("str_SHX:"+ str_SHX)

        bin_SHX = DecToBinary(int(str_SHX, 16))
        #print("bin_SHX", bin_SHX)

        len_x = len(bin_SHX)
        #print("lenx" ,len_x)

        #target_str_bin = ''.join(format(ord(i), '08b') for i in target_string)
        #print("target string:" + target_string)
        #print(target_str_bin)
        len_target_str = len(target_string)
        #print("len_target_str:" , len_target_str)

        strX_ind = 256 - len_target_str
        target_str_ind = 0
        i = strX_ind
        j = target_str_ind

        while len_target_str > 0:

            if target_string[j] == bin_SHX[strX_ind]:
                j += 1
                strX_ind += 1
                if strX_ind > 255:
                    #print(x)
                    str_X = x.encode('utf-8')
                    return str_X
            else:
                break;

   # return( nonce )


#print(hash_preimage('111100'))

