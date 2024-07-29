def reve_numstr(num):
    return int(str(num)[::-1])


exmp_num = 12345
reversed_num = reve_numstr(exmp_num)
print(f'After Reversing {exmp_num} is:',reversed_num)