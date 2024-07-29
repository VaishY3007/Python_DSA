import pytest
from Array_SomeNum import consecutive_values, isPrime, CountMaxZeros

@pytest.fixture
def prime_array():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

@pytest.fixture
def composite_array():
    return [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

@pytest.fixture
def mixed_array():
    return [2, 3, 0, 7, 0, 11, 0, 13, 17, 0]

def test_consecutive_values():
    expected_result = [2, 3, 4, 5, 6]
    result_array = consecutive_values(2, 5)
    result_list = list(result_array)  # Convert array to list
    assert result_list == expected_result


def test_isPrime(prime_array, composite_array):
    for num in prime_array:
        assert isPrime(num) == True
    for num in composite_array:
        assert isPrime(num) == False
    assert isPrime(0) == False
    assert isPrime(1) == False

def test_CountMaxZeros():
    input_array = [0, 1, 0, 0, 2, 0, 0, 0, 3, 0, 4, 5, 0, 0]
    max_zeros, start_num, end_num = CountMaxZeros(input_array)
    assert max_zeros == 3
    assert start_num == -1
    assert end_num == 3



