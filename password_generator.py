from random import randint

special_chars= [
    33, 35, 36, 37, 38,
    42, 43, 45, 46, 58,
    63, 64, 94, 95, 126
]
lower_chars_range= [97, 122]
upper_chars_range= [65, 90]
number_chars_range= [48, 57]

def special_selector():
    return chr(special_chars[randint(0, len(special_chars) -1)])

def lower_selector():
    return chr(char_selector(lower_chars_range[0], lower_chars_range[1]))

def upper_selector():
    return chr(char_selector(upper_chars_range[0], upper_chars_range[1]))

def number_selector():
    return chr(char_selector(number_chars_range[0], number_chars_range[1]))

def char_selector(a, b):
    return randint(a, b)

def selector(x):
    return{
        0: number_selector(),
        1: special_selector(),
        2: lower_selector(),
        3: upper_selector()
    }[x]

def gen_pass(pass_size=8, pwd=""):
    if pass_size <= 0:
        return pwd
    pwd += selector(randint(0, 3))
    return gen_pass(pass_size -1, pwd)
    
def make_pass(pass_size):
    return gen_pass(pass_size)

print(make_pass(36))