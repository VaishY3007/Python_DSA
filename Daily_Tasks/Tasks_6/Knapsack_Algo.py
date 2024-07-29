def tableKnapsack(cap, weight, val, n):

    tbl = [[0 for x in range(cap + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for w in range(cap + 1):
            if i ==0 and w ==0:
                tbl[i][w] =0
            elif weight[i-1] <= w:
                tbl[i][w] = max(val[i-1] + tbl[i-1][w-weight[i-1]], tbl[i-1][w])
            else:
                tbl[i][w] = tbl[i-1][w]
                
    selectedItems = []
    w = cap
    for i in range(n, 0, -1):
        if tbl[i][w] != tbl[i-1][w]:
            selectedItems.append(weight[i-1])
            w -= weight[i-1]

    return tbl[n][cap], selectedItems[::-1]

if __name__ == '__main__':
    weight = [2,3,5,10]
    profit = [100,120,150,400]
    capacity = 7
    maxProfit, selectedItems = tableKnapsack(capacity, weight, profit, len(weight))
    print(f'Selected items from {weight}--> {selectedItems}')
    print(f'Maximu Profit {maxProfit}')