num= 0
temp= 0
for x in range(10):
    if x > 1:
        temp= num
        num= num + temp
    elif x == 0:
        temp= 1
        num= num + temp
    print(num)
print("done =D")