#iterattools, product, permutations, combination, accumulation, groupby, and infintie iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator
a = [1,2]
b = [3,4]
c = [5]
p1 = product(a,b)
print(list(p1))
p2 = product(a,c, repeat=2)
print(list(p2))

a = [1,2,3,4]
perm1 = permutations(a)
print(list(perm1))
perm2 = permutations(a,2)
print(list(perm2))

com1 = combinations(a, 2)
print(list(com1))
com2 = combinations_with_replacement(a,2)
print(list(com2))

ac1 = accumulate((a))
print(list(ac1)) #[1, 3, 6, 10]
ac2 = accumulate((a), func=operator.mul)
print(list(ac2)) # [1, 2, 6, 24]

def negative_number(num):
    return num<0

num1 = [-1,-4,-2.5, 9.9, -45, 0]
g1 = groupby(num1, key= negative_number)
for key,value in g1:
    print(key, list(value))

g1 = groupby(num1, key=lambda x: x < 0)
for key,value in g1:
    print(key, list(value))

a = [1,2,3,4]
group_obj = groupby(a, key=lambda x:x<3)
for key, value in group_obj:
    print(key, list(value))

persons = [{"name":"a", "age":25}, {"name":"b", "age":25}, {"name":"c", "age":26}, {"name":"d", "age":27}]
group_age = groupby(persons, key=lambda x: x["age"])
for key, value in group_age:
    print(key, list(value))

for i in count(10,2):
    print(i)
    if i >100:
        break
a1 = [1,2,3,4,5]
count = 0
for i in cycle(a1):
    count = count+1
    print(i)
    if count >10:
        break

for i in repeat(100,5):
    print(i)
