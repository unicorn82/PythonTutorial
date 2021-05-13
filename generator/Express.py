import sys
g1 = (i for i in range(20) if i%2 == 0)

print(g1) # it is a generator
for i in g1:
    print(i)
print(list(g1))

l1 = [i for i in range(20) if i%2 == 0]

print(l1) #it is a list


g2 = (i for i in range(2000000) if i%2 == 0)

l2 = [i for i in range(2000000) if i%2 == 0]

print(sys.getsizeof(g2))
print(sys.getsizeof(l2))