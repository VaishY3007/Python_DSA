 
def myHashingFun(key, maxLen):
    sum = 0
    for i in key:
        sum += ord(i)
    print(f'sum: {sum}',end = ' ')    
    return (sum % maxLen)
 
if __name__ == '__main__':
    key = 'Different String'
    res = myHashingFun(key,101)
    print(f'sum: {key} and num below {res}')
 
    key = 'ABC'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
 
    key = 'DEFT'
    res = myHashingFun(key,11)
    print(f'sum: {key} and num below {res}')
    #[] --> 100 elements