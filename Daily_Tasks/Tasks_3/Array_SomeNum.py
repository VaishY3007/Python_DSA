from array import array

def consecutive_values(first_value, total_values):
    arr = array('i', [0] * total_values)
    arr[0] = first_value
    for i in range(1, total_values):
        arr[i] = first_value + i
    return arr

def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def CountMaxZeros(lst):
    max_zeros = 0
    count_zeros = 0
    start_num = None
    end_num = None
    for num in lst:
        if num == 0:
            count_zeros += 1
        else:
            if count_zeros > max_zeros:
                max_zeros = count_zeros
                start_num = num - count_zeros - 1  
                end_num = num
            count_zeros = 0
    return max_zeros, start_num, end_num


def run_example(first_value):
    total_values = 100
    result_array = consecutive_values(first_value, total_values)
    result_list = list(result_array)

    print("Original Consecutive Values Array:", result_list)

    # Filtering prime numbers and updating the array
    for i in range(total_values):
        if not isPrime(result_array[i]):
            result_array[i] = 0

    print("Resulting Array:", result_array)

    # Calculate and display maximum count of zeros between numbers
    max_zeros, start_num, end_num = CountMaxZeros(result_array)
    print("Maximum count of zeros between numbers:", max_zeros)
    print("Start number:", start_num)
    print("End number:", end_num)

# Example usage:
if __name__ == "__main__":
    run_example(101)  # Provide the first value here
