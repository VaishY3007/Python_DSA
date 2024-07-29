def bitwise_AND_of_subsets(nums):
    result = float('inf')  # Initialize result with infinity
    n = len(nums)

    # Iterate through all possible subsets
    for i in range(1, 1 << n):
        subset = []
        bitwise_and = None  # Initialize bitwise AND with None
        # Construct the subset and calculate its bitwise AND
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
                if bitwise_and is None:
                    bitwise_and = nums[j]
                else:
                    bitwise_and &= nums[j]  # Perform bitwise AND operation
        # Print the subset and its bitwise AND
        print(subset, "-->", bitwise_and)
        # Update the result if the current subset's AND is smaller
        result = min(result, bitwise_and)

    return result

nums = [5, 6, 8]
print("Subsets and their bitwise AND:")
final_result = bitwise_AND_of_subsets(nums)
print("Final result =", final_result)
