# [101, 0, 103, 0, 0, 0, 107, 0, 109, 0, 0, 0, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 131, 0, 0, 0, 0, 0, 137, 0, 139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 0, 151, 0, 0, 0, 0, 0, 157, 0, 0, 0, 0, 0, 163, 0, 0, 0, 167, 0, 0, 0, 0, 0, 173, 0, 0, 0, 0, 0, 179, 0, 181, 0, 0, 0, 0, 0, 0, 0, 0, 0, 191, 0, 193, 0, 0, 0, 197, 0, 199, 0]
 
def zeroCount(start, end, dataList):
    start = 5
    end = 25
    
 
def countMaxZeros(dataList):    
    start = -1
    end = len(dataList)
    max = 0
 
    count = zeroCount(start, end, dataList)
    print(f'start: {start}\t\tend: {end}')
    
    if max < count:
        max = count
    
    return (count, start, end)


if __name__ == '__main__':
    myList = [101, 0, 103, 0, 0, 0, 107, 0, 109, 0, 0, 0, 113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 131, 0, 0, 0, 0, 0, 137, 0, 139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 149, 0, 151, 0, 0, 0, 0, 0, 157, 0, 0, 0, 0, 0, 163, 0, 0, 0, 167, 0, 0, 0, 0, 0, 173, 0, 0, 0, 0, 0, 179, 0, 181, 0, 0, 0, 0, 0, 0, 0, 0, 0, 191, 0, 193, 0, 0, 0, 197, 0, 199, 0]
    res = countMaxZeros(myList)

