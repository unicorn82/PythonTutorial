import random
import secrets
import numpy as np

r1 = random.random()
print(r1)
r2 = random.uniform(1,10)
print(r2)
r3 = random.randint(1,20) #[1,20]
print(r3)
r4 = random.randrange(5,10) #(5,10)
print(r4)
r5_nomral = random.normalvariate(0,1)
print(r5_nomral)
mylist = list("ABCDEFGH")
r6_list = random.choice(mylist)
print(r6_list)
r7_list = random.sample(mylist,3)
print(r7_list) #no duplicate
r8_list = random.choices(mylist, k=3)
print(r8_list) #could be duplicate like ['E', 'A', 'A']
random.shuffle(mylist)
print(mylist)

#random seed, randome is reproducible
random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10)) #same value

random.seed(2)
print(random.random())
print(random.randint(1,10)) #same value
#not good for secure reason
random.seed(1)
print(random.random())
print(random.randint(1,10)) #same value

#secrets
s1 = secrets.randbelow(10)
print(s1)
s2 = secrets.randbits(4) #0000 - 1111
print(s2)
mylist2 = list("ABCDEFHG")
s3 = secrets.choice(mylist2)
print(s3)

#numpy
n1 = np.random.rand(3)
print(n1)
n2 = np.random.randint(0, 10,3)
print(n2)
n3 = np.random.randint(0,10,(3,4))
print(n3)
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,4))
np.random.seed(1)
print(np.random.rand(3,4))
