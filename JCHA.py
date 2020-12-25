import math;
import sys;

class JCHA:
    """
    Author: Cyber Goose
    Created: 2020-12-24 (too early in the morning... )
    Recreation of DIY_HASHER.py Using my own hashing algo, for fun.
    This is just for fun and not ment to be used for sensitive data.
    Intended for practicing and understand simple encryption methods.
    """

    text_length= 0;
    def __init__(self) -> None:
        super().__init__();

    def hash_str(self, clear_text):
        text_length= len(clear_text);
        clear_text= clear_text.replace(' ', '');
        text_hashed= '';

        for text_char in clear_text:
            x= (ord(text_char)**2)
            unicode_value= (ord(text_char) + x);
            temp= int(math.pow( unicode_value, text_length));
            temp<< temp % text_length;
            text_hashed+= hex(temp).replace('0x', '');

        text_hashed= text_hashed.replace('0', '');
        byte_size= sys.getsizeof(text_hashed);
        return self.setBytes(text_hashed, byte_size);

    def setBytes(self, hash, byte_size):
        
        if(byte_size != 128):
            if(byte_size > 128):
                while(byte_size != 128):
                    hash= hash[:-1];
                    byte_size= sys.getsizeof(hash);
            else:
                while(byte_size != 128):
                    temp= sys.getsizeof(hash) % len(hash);
                    hash+= hex(sys.getsizeof(hash) + temp).replace('0x', '');
                    byte_size= sys.getsizeof(hash);
        return hash;


    def compare(self, clear_str, hashed_str):
        return (self.hash_str(clear_str) == hashed_str);


text_in= input("Enter text to hash:\n");
jcha= JCHA();
hashed_text= jcha.hash_str(text_in);
print(jcha.compare(input("Compare text:\n"), hashed_text));
print(hashed_text);