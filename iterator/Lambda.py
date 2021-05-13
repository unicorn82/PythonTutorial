#lambda expression
from functools import reduce
add10 = lambda x: x+10
print(add10(5))

mult = lambda x, y : x*y
print(mult(4,6))

point_2d = [(1,5), (6,-7), (-4,8), (11,-5)]
point_sortByx = sorted(point_2d)
print(point_sortByx) #[(-4, 8), (1, 5), (6, -7), (11, -5)]
point_sortByy = sorted(point_2d, key=lambda x: x[1])
print(point_sortByy) #[(6, -7), (11, -5), (1, 5), (-4, 8)]
point_sortBySum = sorted(point_2d, key=lambda x: x[0]+x[1])
print(point_sortBySum) #[(6, -7), (-4, 8), (1, 5), (11, -5)]

def sort_by_mult(x):
    return x[0]*x[1]
point_sortByMult = sorted(point_2d, key=sort_by_mult)
print(point_sortByMult)

#map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x:x*2,a)
print(list(b)) #[2, 4, 6, 8, 10]
c = [x*3 for x in a]
print(c)

#filter(func, seq)
even = filter(lambda x:x%2==0, a)
print(list(even))
even2 = [x for x in a if x%2 == 0]
print(list(even2))

#reduce(func, seq)
product = reduce(lambda x,y:x*y,a)
print(product)
