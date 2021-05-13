import functools
def start_end_decorator (func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start function")
        result = func(*args, **kwargs)
        print("end function")
        return result

    return wrapper;


def print_msg():
    print("this is a message")

print_msg()

#call wrapper without decorator
func = start_end_decorator(print_msg)
func()

#call with decorator

@start_end_decorator
def print_new_msg():
    print("this is a new message")
print_new_msg()

#call  with parameter

@start_end_decorator
def add5(x):

    return x+5

result = add5(10)
print("result ", result)

print(help(add5))
print(add5.__name__)
