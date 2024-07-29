def fun(first, second, *args, **kwargs):
    print(f'fun() called')
    print(f'\t\tWith : first: {first}, \tsecond: {second}')
    print(f'\t\tWith : args: {args}')
    print(f'\t\tWith : kwargs: {kwargs}')
    
fun(10,20,30,40,50, 'test', 'rest', 'best', a=1, b=20, p=30, name='Virat Babu')