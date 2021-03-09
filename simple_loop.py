'''
Playing with recursion
simple for loop
'''

def loop(start_at, stop_at, step= 1):
    if(start_at >= stop_at):
        return start_at + step
    print(start_at)
    return loop(start_at + step, stop_at, step)

# print(recur(0, 5))
loop(0, 5)
print('\n')
loop(1, 10, 2)
print('\n')
loop(-1, 23, 3)