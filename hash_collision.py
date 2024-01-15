import binascii
import hashlib
import os
import string
import random
import binascii

def DecToBinary(num):
    #return bin(num).replace("0b", "")
    return bin(num)[2:].zfill(256)

def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    finding = -1
    while finding < 0:

        rand1 = random.randrange(1, 1000,1)
        #print(rand1)
        letters = string.ascii_letters
        x = ''.join(random.choices(string.ascii_letters, k = rand1))
        #print(x)

        rand2 = random.randrange(1, 1000, 1)
        #print(rand2)
        y = ''.join(random.choices(string.ascii_letters, k=rand2))
        #print(y)

        str_SHX = hashlib.sha256(x.encode('utf-8')).hexdigest()
        #print("str_SHX:"+ str_SHX)
        str_SHY = hashlib.sha256(y.encode('utf-8')).hexdigest()
        #print("str_SHY:"+ str_SHY)

        bin_SHX = DecToBinary(int(str_SHX , 16))
        #print("bin_SHX", bin_SHX)
        bin_SHY = DecToBinary(int(str_SHY , 16))
        #print("bin_SHY", bin_SHY)

        len_x = len(bin_SHX)
        #print("lenx" ,len_x)
        len_y = len( bin_SHY)
        #print("leny" ,len_y)

        index_start = 256 - k
        #print("index_start:" , index_start)

        index_checked = index_start
        i = index_start

        while k <= 1:
            if bin_SHX[255] == bin_SHY[255]:
                str_X = x.encode('utf-8')
                str_Y = y.encode('utf-8')
                print(str_X, str_Y)
                return (str_X, str_Y)
            else:
                break

        while k >1:
        #for i in range(index_start, 255):
           # print("gets here")
            if bin_SHX[i] != bin_SHY[i]:
                #print("bin_SHX[i]:",i, bin_SHX[i])
                #print("bin_SHXY[i]:",i,  bin_SHY[i])
                break
            elif bin_SHX[i] == bin_SHY[i]:
                i +=1
                index_checked += 1
                if index_checked >= len_x :
                    str_X = x.encode('utf-8')
                    str_Y = y.encode('utf-8')
                    #print(str_X, str_Y)
                    #print("bin_SHX", bin_SHX)
                    #print("bin_SHY", bin_SHY)
                    return (str_X, str_Y)


#hash_collision(4)
