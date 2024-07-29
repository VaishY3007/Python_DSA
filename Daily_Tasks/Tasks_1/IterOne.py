myList = list(range(0,50,5))
myIter = iter(myList)

print(myIter)
for i in range(len(myList)):
    print(next(myIter), end=' ')