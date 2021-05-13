#Sets: unordered, mutable, no duplicates


#create
myset1 = {1,2,3,3,2,1}
print(myset1) #{1, 2, 3}

myset2 = set("hello")
myset3 = set([1,2,3])
print(myset2) #{'e', 'o', 'l', 'h'}
print(myset3)
emptySet = set()
print(type(set()))
emptySet.add(1)
emptySet.add(2)
emptySet.add("sample")
emptySet.discard(1)
emptySet.pop()
print(emptySet)
for i in emptySet:
    print(i)

print("sample" in emptySet)

#set operation
odd = {1,3,5,7,9}
even = {2,4,6,8,10}
prime = {2,3,5,7}
print(odd.union(even))
print(odd.intersection(prime))
setA = {1,2,3,5,6,7,8,9}
setB = {1,2,4,5,7,10,11}
print(setA.difference(setB)) #{8, 9, 3, 6}
print(setB.difference(setA)) #{10, 11, 4}
print(setA.symmetric_difference(setB)) #{3, 4, 6, 8, 9, 10, 11}
setA.update(setB) #not like union, update function modify setA instead of return
print(setA) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
setA = {1,2,3,5,6,7,8,9}
setB = {1,2,4,5,7,10,11}
setA.intersection_update(setB) #{1, 2, 5, 7}
print(setA) #{1, 2, 4, 5, 7, 10, 11}

setA = {1,2,3,5,6,7,8,9}
setB = {1,2,4,5,7,10,11}
setA.difference_update(setB) #{3, 6, 8, 9}
print(setA) #{1, 2, 4, 5, 7, 10, 11}

setA = {1,2,3,5,6,7,8,9}
setB = {1,2,4,5,7,10,11}
setA.symmetric_difference_update(setB)
print(setA) #{3, 4, 6, 8, 9, 10, 11}

setA = {1,2,3,5,6,7,8,9}
setB = {1,2,3}
print(setA.issuperset(setB)) #True
print(setB.issubset(setA)) #True
setC = {7,8}
print(setB.isdisjoint(setA)) #False
print(setC.isdisjoint(setB)) #True

setA = {1,2,3,4,5,6}
setC = setA.copy()
setD = set(setA)
setB = setA
setB.add(7)
print(setA) #{1,2,3,4,5,6,7}
print(setC) #{1,2,3,4,5,6}
print(setD) #{1,2,3,4,5,6}

setF = frozenset([1,2,3])
#setF.add(4) AttributeError: 'frozenset' object has no attribute 'add'





