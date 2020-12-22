# INCOMPLETE 

import math

str_to_hash= "Hello"

def JCHA(mstr):
    length= len(mstr);
    temp_array= [];
    jcha= '';
    
    for x in mstr:
        temp_array.append(hex(int(math.pow(ord(x), length))));
        
    for item in temp_array:
        x= str(item).split('0x');
        jcha += x[1];
    return jcha;

print(JCHA(str_to_hash));