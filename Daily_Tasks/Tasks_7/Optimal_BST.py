def OBSTree(keys, freqs):
    keysLen = len(keys)
    costTable = [[0] * keysLen for _ in range(keysLen)]
    rootTable = [[0] * keysLen for _ in range(keysLen)]
    
    for i in range(keysLen):
        costTable[i][i] = freqs[i]
        
    print('Initial cost table:')
    for row in costTable:
        print(row)
        
    for length in range(2, keysLen + 1):
        for i in range(keysLen - length + 1):
            j = i + length - 1
            costTable[i][j] = float('inf')
            sumTemp = sum(freqs[i:j + 1])
            
            for r in range(i, j + 1):
                cost_left = costTable[i][r - 1] if r > i else 0
                cost_right = costTable[r + 1][j] if r < j else 0
                c = cost_left + cost_right + sumTemp
                if c < costTable[i][j]:
                    costTable[i][j] = c
                    rootTable[i][j] = r
    
    print('Final cost table:')
    for row in costTable:
        print(row)
        
    print('Root table:')
    for row in rootTable:
        print(row)
    
    return costTable, rootTable
        
def buildTree(keys, root, i, j):
    if i > j:
        return None
    elif i == j:
        return {'key': keys[i], 'left': None, 'right': None}
    else:
        rootIndex = root[i][j]
        rootkey = keys[rootIndex]
        leftTree = buildTree(keys, root, i, rootIndex - 1)
        rightTree = buildTree(keys, root, rootIndex + 1, j)
        return {'key': rootkey, 'left': leftTree, 'right': rightTree}
    
if __name__ == '__main__':
    keys = [10, 15, 20]
    freqs = [70, 50, 30]
    cost, root = OBSTree(keys, freqs)
    print(f'Minimum cost: {cost[0][len(keys)-1]}')
    OBST = buildTree(keys, root, 0, len(keys) - 1)
    print('Optimal Binary Search Tree:', OBST)
