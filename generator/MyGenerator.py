def mygenerator():
    yield 1
    yield 2
    yield 3

g1 = mygenerator()

print(g1)

for i in g1:
    print(i)

g2 = mygenerator()
print(next(g2))
print(next(g2))
print(next(g2))

g3 = mygenerator()
print(sum(g3))

g4 = mygenerator()
print(sorted(g4))

def countdown(num):
    while num > 0:
        yield num
        print(f"start {num}")
        num -= 1

print(countdown(5)) #<generator object countdown at 0x7fb3231cb6d0>

g1 = countdown(10)
print(next(g1)) #10
#it stops at yield statement

print(next(g1)) #start 10 /n 9
