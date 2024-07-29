def find_non_repeating_elements(arr):
    xor_result = 0
    for num in arr:
        xor_result ^= num
    
    rightmost_set_bit = xor_result & -xor_result
    
    group1 = 0
    group2 = 0
    for num in arr:
        if num & rightmost_set_bit:
            group1 ^= num
        else:
            group2 ^= num
    
    repeating_numbers = set()
    for num in arr:
        if num != group1 and num != group2 and arr.count(num) > 1:
            repeating_numbers.add(num)
    
    non_repeating_elements = [num for num in arr if arr.count(num) == 1]
    
    return non_repeating_elements, list(repeating_numbers)

# Example usage
# arr = [10,10,10,10,2,2,4,5,4,10,2,3]
arr = [4, 2, 4, 5, 2, 3, 3, 1]
non_repeating_elements, repeating_numbers = find_non_repeating_elements(arr)
print("Non-repeating elements:", non_repeating_elements)
print("Repeating elements:", repeating_numbers)
