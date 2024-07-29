'''
generator functions
'''
# def generateNums():
#     lst = []
#     for i in range(10):
#         lst.append(i)
#     return lst
# print(type(generateNums()))
# for var in generateNums():
#     print(var, end=' ')

def genFun():
    # print("One")
    yield 1
    # print("Two")
    yield 2
    # print("Three")
    yield 3

resGen = genFun()

for i in resGen:
    print(i, end= ' ')

'''
print(next(resGen))
print(next(resGen))
print(next(resGen))
print(next(resGen))
'''