

fun = lambda: print("Hello, world!")
fun()

x = lambda a: a*a
print(x(5))

fun1 = lambda a, b: a+b
print(fun1(10,20))

def funOne(n):
    return lambda num: num **n
sqr = funOne(3)
print(sqr(10)) # 10 is the Value of num