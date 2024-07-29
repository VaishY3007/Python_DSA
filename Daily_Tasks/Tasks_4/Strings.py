myStr = 'Give in a string'
print(f'myStr = {myStr}')

'''slicing & Reverse the string'''
str = myStr[::-1]
print(str)




'''Reverse the String using reverse the fucntion'''
myList = list(myStr)
print(f'myList = {myList}')
myList.reverse() 
reversedStr = ''.join(myList)
print("Reversed str using function:", reversedStr)

'''Reversing the String Using the Loop'''
reversed_str = ""
for char in myStr:
    reversed_str = char + reversed_str
print("Reversed str using Loop:", reversed_str)

# myListOne = [*myStr]
# print(f'myListOne = {myListOne}')


# lst = []
# for i in myStr:
#     print(f'{i}', end = ' ')
#     lst.append(i)
#     print(lst)
    
# myListTwo = []
# myListTwo.extend(myStr)
# print(f'\nmyListTwo: {myListTwo}')

