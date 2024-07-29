def fact_recur(num):
    if num < 0:
        raise ValueError("Factorail is not for Negative Numbers")
        
    if num==0 or num==1:
        return 1
    return num* fact_recur(num-1)

num = 5    
print(f'The Factorial of {num} is:',fact_recur(5))