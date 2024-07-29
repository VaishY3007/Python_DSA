from random import randint

def mySort(dataList):
    for i in range(len(dataList)):
        for j in range(i + 1, len(dataList)):
            if dataList[i] > dataList[j]:
                dataList[i], dataList[j] = dataList[j], dataList[i]

def mySearch(dataList, data):
    pos = 0
    while pos < len(dataList):
        if dataList[pos] == data:
            return pos
        pos += 1
    return -1

dataList = [randint(1, 100) for _ in range(10)]

print("Before sorting:", dataList)

mySort(dataList)

print("After sorting:", dataList)

search_value = int(input("\nEnter the value to search for: "))
print("Searching for value:", search_value)
result = mySearch(dataList, search_value)
if result != -1:
    print(f"Found {search_value} at index {result}.")
else:
    print(f"{search_value} not found in the list.")
