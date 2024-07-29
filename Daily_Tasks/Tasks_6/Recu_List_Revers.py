def reverse_list(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start >= end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end -1)
    
exmp_list = [1,2,3,4,5]
reverse_list(exmp_list)
print(exmp_list)