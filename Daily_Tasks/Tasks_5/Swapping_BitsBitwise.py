def swap_bits(n, i, j):
    if ((n >> i) & 1) != ((n >> j) & 1): #Right Shift Operation
        bit_mask = (1 << i) | (1 << j)  #Left Shift Operation
        n = n ^ bit_mask  # XOR Operation
    return n

if __name__ == "__main__":
    result = swap_bits(10, 1, 2)
    print("Result:", result)
