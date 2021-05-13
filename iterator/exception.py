#Error and Exception
x = -5
# if x<0:
#     raise Exception("x should be positive")

# assert (x>0), "x should be positive"

try:
    x = 10/0
except Exception as e:
    print(e) #division by zero

try:
    x = 10/0
except ZeroDivisionError as e:
    print("Catch ZeroDivisionError")
    try:
        s = 10+"str"
    except TypeError as e:
        print(e)
    else:
        print("everything is fine")
    finally:
        print("inner finally")
else:
    print("everything is fine")
finally:
    print("outer finally")

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def value_test(value):
    if value >100:
        raise ValueTooHighError("your value is too high")
    if value < 10:
        raise ValueTooLowError("your value is too low", value)

try:
    value_test(200)
except ValueTooHighError as e:
    print(e)

try:
    value_test(8)
except ValueTooLowError as e:
    print(e.message+ " value is " +str(e.value))
    print(e.message, e.value)

