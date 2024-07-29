def fibboGen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
fiboseries = fibboGen()

for i in range(10):
    print(next(fiboseries), end=' ')




'''
cnt =0
for i in fiboseries:
    print(f'{cnt} --> {i}')
    if cnt > 10:
        break
    cnt += 1'''