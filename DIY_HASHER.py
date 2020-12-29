#   INCOMPLETE
#   Moved to JCHA.py

import math
import sys

str_to_hash= input("Enter a string to hash:\n");

def JCHA(my_str):
    my_str= my_str.replace(' ', '');
    length= len(my_str);
    jcha= '';

    for my_char in my_str:
        temp= int(math.pow( (ord(my_char) + 200), length));
        temp<< temp % length;
        print(sys.getsizeof(temp));
        jcha+= hex(temp).replace('0x', '');
    
    jcha= jcha.replace('0', '');
    byte_size= sys.getsizeof(jcha);

    if(byte_size != 128):
        if(byte_size > 128):
            while(byte_size != 128):
                jcha= jcha[:-1];
                byte_size= sys.getsizeof(jcha);
        else:
            counter= 0;
            while(byte_size != 128):
                jcha+= jcha[counter];
                counter+= 1;
                byte_size= sys.getsizeof(jcha);
    print(sys.getsizeof(jcha));
    return jcha;

print(JCHA(str_to_hash));