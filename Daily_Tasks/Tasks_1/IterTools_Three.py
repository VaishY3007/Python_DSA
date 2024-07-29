from itertools import product, permutations, combinations

myIter = product('XYZ', repeat=2)

for i in myIter:
    print(i, end=' ')
print("\n........Permutations....................")

myIterTwo = permutations('XYZ', 2)

for i in myIterTwo:
    print(''.join(i), end=' ')
    
print("\n...........Combinations.................")
   
myIterThree = combinations('XYZ', 2)

for i in myIterThree:
    print(''.join(i), end=' ')