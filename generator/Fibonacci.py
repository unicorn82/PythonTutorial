def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

fib1 = fibonacci(20)
for i in fib1:
    print(i)