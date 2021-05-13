#Dictionary, key-value pairs, unordered, mutable
#create dictionary
my_dict1 = {"name": "Max", "age": 34, "city": "New York"}
print(my_dict1)
print(my_dict1["name"])
my_dict2 = dict(name="Max", age=34, city="New York")
print(my_dict2)
print(my_dict2["age"])
#my_dict2["lastname "] #Key ERROR
my_dict3 = my_dict2
my_dict3["email"] = "xxx@yyy.com"
print(my_dict2)
print(my_dict3) #same value
my_dict4 = my_dict3.copy()
del(my_dict4["email"])
print(my_dict4)
my_dict5 = dict(my_dict3)
print(my_dict5.pop("age")) #34
print(my_dict5) #{'name': 'Max', 'city': 'New York', 'email': 'xxx@yyy.com'}
my_dict5.popitem()
print(my_dict5) #{'name': 'Max', 'city': 'New York'}

#operation
my_dict6 = my_dict1.copy()
print("name" in my_dict6) #True
print("last" in my_dict6) #False

try:
    print(my_dict6["lastname"])
except:
    print("error")

#loop
for key in my_dict6:   #my_dict6.keys()
    print(key+"->"+ str(my_dict6[key]))
for value in my_dict6.values():
    print(value)
for key,value in my_dict6.items():
    print(key+"->" + str(my_dict6[key]))

#merge
my_dict7 = dict(my_dict1)
my_dict8 = {"name": "New", "age": 50, "lastName": "mylast"}
my_dict7.update(my_dict8)
print(my_dict7)
print(my_dict8)

#key is number
my_dict9 = {1:8, 3:90, 5:125}
print(my_dict9[3])  #3 is not an index

#key is tuple, only tuple, no list
my_tuple = ("tupe", "is key")
tuple_dict = {my_tuple:"value"}
print(tuple_dict)



