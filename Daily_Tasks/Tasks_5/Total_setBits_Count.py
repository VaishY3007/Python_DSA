def count_set_bits(n):
    count = 0
    while n > 0:
        count += n % 2
        n = n // 2
    return count

def count_total_set_bits(n):
    total_count = 0
    for i in range(1, n + 1):
        count = count_set_bits(i)
        print(f'The count of set bits in {i} is {count}')
        total_count += count
    print(f'Total set bits count from 1 to {n}: {total_count}')

n = 10
count_total_set_bits(n)
