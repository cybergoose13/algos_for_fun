# INCOMPLETE 

import math

str_to_hash= "Hello"

def JCHA(mstr):
    length= len(mstr);
    print("Length of string: " + str(length));
    # make and set string of each char's binary value.
    binary_string= ('' + '\n'.join(format(ord(i), 'b') for i in mstr));
    print("Binary String: " + binary_string);

    # split the binary string into an array per char.
    binary_array= binary_string.split('\n');
    print("Binary Array: " + str(binary_array));

    temp= 0;
    temp_array= [];
    # loop through the binary string values
    for c in binary_array:
        # num= int(c) * length;
        # num_array= str(num);

        for n in c:
            temp += int(n);

        # temp_array.append(hex(temp));
        
        print("temp is: " + str(temp));
        temp_array.append( hex( int(math.pow(temp, length)) ));
        temp=0;


    return temp_array;

print(JCHA(str_to_hash));