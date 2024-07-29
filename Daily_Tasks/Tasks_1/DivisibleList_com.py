numbers = list(range(1, 1001))

for divisor in range(5, 10):
    divisible_numbers = [num for num in numbers if num % divisor == 0]
    print(f"{divisor}: {divisible_numbers}")
