def fun(arg):
    # print(f'arg: {arg}', end=' ')
    return arg + 101

ret = map(lambda x: x+101, [1,2,3,4,5])

print(ret)  # printing the map object
for i in ret: #iterating through map object
    print(i)
          