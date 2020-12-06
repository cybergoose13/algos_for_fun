_MIN= ord('a') - 1
_MAX= ord('z')
_SPACE= ord(' ')

def cipher(letter, rot):
    if ord(letter) == _SPACE:
        return letter
    char_num= ord(letter) + rot
    if char_num > _MAX:
        letter= chr((char_num - _MAX) + _MIN)
    else:
        letter= chr(char_num)
    return(letter)


def cipher_word(text, rot=13):
    text= text.lower()
    word= ''
    for l in text:
        word += cipher(l, rot)
    return word


print(cipher_word('abc', 1))
print(cipher_word('test'))
print(cipher_word('TEST'))
print(cipher_word('hello friend', 5))