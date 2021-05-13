#String: ordered, immutable, text representation
from timeit import default_timer as timer
string1 = 'I\'m a developer'
string2 = "It is a string"
string3 = '''
    it is a long text
    with multiple lines \
    or same line
'''
print(string3)

print(string2[0])
print(string2[-2])
#string2[0] = "i" #TypeError: 'str' object does not support item assignment
print(string2[1:5]+" "+string2[:]+" "+string2[:5]+" ")
print(string2[::-1]) #reverse string

for i in string1:
    print(i)

print("d" in string1)

print("   string   ".strip())
print(string1.upper()+string1.lower())

mystring = "hello world"
print(mystring.startswith("hello"))
print(mystring.endswith("world"))
print(mystring.find("wor"))
print(mystring.count("o"))
print(mystring.replace("world", "universe"))
mystring1 = "how are you doing"
mylist = mystring.split() #default splitter is space
print(mylist)
mystring1 = "how,are,you,doing"
mylist1 = mystring1.split(",") #default splitter is space
print(mylist1)
print("|".join(mylist1))


mylist2 = ["a"]*1000000
start = timer()
print("".join(mylist2))
stop = timer()
print(stop-start)

name = "Tom"
age = 53
height = 1.80345
old_format_log = "the person is %s" % name
print(old_format_log)
new_format_log1 = "the person is {} and age is {}, height is {:.2f}".format(name, age, height)
print(new_format_log1)
new_format_log2 = f"the person is {name} and age is {age}, height is {height :.2f}"
print(new_format_log2)

