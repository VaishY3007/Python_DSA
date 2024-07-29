def subSetSolver(mySet, start, sumRequired, path, result):
    if sumRequired == 0:
        result.append(path[:])  # Append a copy of the path, not the original list
        return
    
    if sumRequired < 0 or start >= len(mySet):  # Consider when start exceeds the length of the set
        return
    
    for i in range(start, len(mySet)):
        if i > start and mySet[i] == mySet[i - 1]:
            continue
        subSetSolver(mySet, i + 1, sumRequired - mySet[i], path + [mySet[i]], result)  # Append the current element to the path, not add it
    return result  # Return the result after the loop

def subSetSum(mySet, sumRequired):
    mySet.sort()
    result = []
    subSetSolver(mySet, 0, sumRequired, [], result)
    return result

if __name__ == '__main__':
    mySet = [2, 4, 3, 6, 5, 8]
    sumRequired = 10
    print(f'subsets : {subSetSum(mySet, sumRequired)}')
