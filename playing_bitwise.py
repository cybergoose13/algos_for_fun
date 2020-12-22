#Playing with bitwise operators
#trying to understand them

def binAnd(a, b):
    c= (a & b);
    print("Binary AND");
    print(format(c, 'b'));
    return c;

def binOr(a, b):
    c= (a | b);
    print("Binary OR");
    print(format(c, 'b'));
    return c;

def binXOr(a, b):
    c= (a ^ b);
    print("Binary XOR");
    print(format(c, 'b'));
    return c;

def binOnesComplement(a):
    c= (~a);
    print("Binary Ones Complement");
    print(format(c, 'b'));
    return c;

def binLShift(a, b):
    c= (a << b);
    print("Binary Left Shift");
    print(format(c, 'b'));
    return c;

def binRShift(a, b):
    c= (a >> b);
    print("Binary Right Shift");
    print(format(c, 'b'));
    return c;

a= 13;
b= 25;

binA= format(a, 'b');
binB= format(b, 'b');

print(f"A: {a} in binary {binA}");

print(f"B: {b} in binary {binB}");

print(binAnd(a,b));

print(binOr(a, b));

print(binXOr(a, b));

print(binOnesComplement(a));

print(binLShift(a, 3));

print(binRShift(a, 3));