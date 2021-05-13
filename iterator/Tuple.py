import  sys
import timeit

#create tuple
mytuple1 = (1,"str", 5.0)
print(mytuple1)
mytuple2 = 6, "str2", 23.9
print(mytuple2)
mytuple3 = ("a str not tuple")
print(type(mytuple3)) #<class 'str'>
mytuple4 = ("a real tuple with comma",)
print(type(mytuple4)) #<class 'tuple'>
mytuple5 = tuple(['create tuple', 56, 'from list'])

#index
print(mytuple5) #('create tuple', 56, 'from list')
print(mytuple5[2])
print(mytuple5[-2]) #last second item
#mytuple5[0] = 'new list' #ERROR tuple is immutable
for x in mytuple5:
    print(x)
print(56 in mytuple5) #True

#count, len
mytuple6 = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple6))
print(mytuple6.count('p') + mytuple6.count('0'))
print(mytuple6.index('p'))

#convert to list
mylist = list(mytuple6)
print(mylist)
print(tuple(mylist))

#slicing
s1 = (1,2,3,4,5,6,7,8)
print(s1[2:6]) #(3, 4, 5, 6)
print(s1[:4]) #(1, 2, 3, 4)
print(s1[3:]) #(4, 5, 6, 7, 8)
print(s1[::2]) #(1, 3, 5, 7)
print(s1[::-1]) #(8, 7, 6, 5, 4, 3, 2, 1)

#unpacking
p1 = "max", 34, "CO"
name, age, location = p1 #number of variable match with element in tuple
print(name)
print(age)
print(location)

p2 = 1,2,3,4,5,6
first, *rest, last = p2
print(first) #1
print(rest) #list: [2, 3, 4, 5]
print(last) #6

#compare list and tuple
c_list = [34,'same', 78.0, 'list', 34.98, 'with tuple']
c_tuple = 34,'same', 78.0, 'list', 34.98, 'with tuple'
print(sys.getsizeof(c_list), "bytes") #120 bytes
print(sys.getsizeof(c_tuple), "bytes") #104 bytes

#statement stmt to create list 1000000 times
print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number=1000000))
#statement stmt to create tuple 1000000 times
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number=1000000)) #tuple is faster than list

