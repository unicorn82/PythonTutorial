result = 5 * 7
print(result)

v1 = [0, 1] * 10
print(v1)

v2 = (0, 1) * 10
print(v2)

v3 = "AB" * 10
print(v3)

def foo (a, b, *args, **kwargs):
    print(a, b)
    for i in args:
        print(i)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5,six=6, seven=7)
my_list = [1,2,3,4]
foo(*my_list)

number1 = [1,2,3,4,5,6,7]
number2 = (1,2,3,4,5,6,7,8,9)
*beginning1, last1 = number1
print(beginning1)
print(last1)
*beginning2, last2 = number2
print(beginning2) #is always a list
print(last2)
beginning3, *last3 = number2
print(beginning3)
print(last3)
beginning4, *middle4, secondlast4, last4 = number2
print(beginning4)
print(middle4)
print(secondlast4)
print(last4)

my_tuple1 = (1,2,3)
my_list1 = [4,5,6]
my_set1 = {7,8,9, 10}
print([*my_tuple1, *my_list1, *my_set1])

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
print({**dict_a, **dict_b}) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}