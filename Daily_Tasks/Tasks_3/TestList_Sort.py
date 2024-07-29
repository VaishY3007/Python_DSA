from random import randint
from List_Sort import mySort

def test_sorting():
    # Test case 1: Test sorting with a list of random integers
    dataList = [randint(1, 100) for _ in range(10)]
    sorted_list = sorted(dataList)
    mySort(dataList)
    assert dataList == sorted_list

   

