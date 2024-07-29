def count_set_bits(n):
    count = 0
    while n > 0:
        count += n % 2
        n = n // 2
    return count

n = 5
count = count_set_bits( n)
print(f'The count of set bits in {n} is {count}')
