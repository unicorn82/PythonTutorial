# '''
#  - The different between arguments and parameters
#  - Positional and keyword arguments
#  - Default arguments
#  - Variable-length arguments (*args and **kwargs)
#  - Container unpacking into function arguments
#  - Local vs global arguments
#  - Parameter passing (by value or by reference)
# '''

def foo(a, b, c, d=10):
    print(a, b, c, d)

foo(1,2,3)
foo(b=5, c=6, a=4)
foo(6,7,8,9)

def foo2 (a, b, *args, **kwargs): #arguments and key arguments
    print(a, b)
    print("args")
    print(args)

    for arg in args:
        print(arg)
    print("kwargs")
    for key in kwargs:
        print(f'key = {key} and value = {kwargs[key]}')

foo2(1,2, 3,4, e=5,f=6)

def foo3 (a, b, *, d, e):
    print(a, b, d, e)

foo3(1,2, d=5, e=6)

def foo4 (*args, c, d):
    print(c, d)

foo4(1,2,3, c=4, d=5)

def foo5 (*args, last):
    print(args)
    print(last)

foo5(1,2,3,4, last=10)

def foo6(a,b,c):
    print(a, b, c)

my_list = [1,2,3]
my_tuple = (1,2,3)
foo6(*my_list)
foo6(*my_tuple)
my_dict = {'a': 1, 'b':2, 'c':3}
foo6(**my_dict)

number = 9
def foo_variable():
    global number
    x = number

    number += 1
    print('variable inside function ', x)
    print('variable outside function', number)


foo_variable()

