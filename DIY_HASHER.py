# INCOMPLETE 

import math

str_to_hash= input("Enter a string to hash:\n");

def JCHA(my_str):
    my_str= my_str.replace(' ', '');
    length= len(my_str);
    temp_array= [];
    jcha= '';

    for x in my_str:
        temp_array.append(hex(int(math.pow((ord(x) + 200) , length))));
        
    for item in temp_array:
        jcha += item.replace('0x', '');
        
    return jcha;

print(JCHA(str_to_hash));