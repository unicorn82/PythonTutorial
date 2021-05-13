import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1

    return nums

#data are stored in the list in memory
print(firstn(10))
print(sum(firstn(20)))
print(sorted(firstn(5)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

g1 = firstn_generator(10)
print(next(g1))
print(next(g1))
print(sum(firstn_generator(20)))
print(sorted(firstn_generator(5)))

#compare
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
