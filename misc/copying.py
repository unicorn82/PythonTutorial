import copy
'''
 - shallow copy, only one level deep, only reference of nested child objects
 - deep copy, full independent copy 
'''
org1 = [1,2,3,4,5]
cpy1 = org1
cpy1[0] = -10
print(org1) #[-10, 2, 3, 4, 5]
print(cpy1) #list is mutable

org2 = [1,2,3,4,5]
cpy2 = copy.copy(org2)
cpy3 = org2.copy()
cpy4 = list(org2)
cpy5 = org2[:]
org2[0] = -10

print(org2)
print(cpy2)
print(cpy3)
print(cpy4)
print(cpy5)

org_nest1 = [[1,2,3,4,5],[6,7,8,9]]
cpy_shallow = copy.copy(org_nest1)
cpy_deep = copy.deepcopy(org_nest1)
org_nest1[0][1] = -10
print(org_nest1) #[[1, -10, 3, 4, 5], [6, 7, 8, 9]]
print(cpy_shallow) #[[1, -10, 3, 4, 5], [6, 7, 8, 9]]
print(cpy_deep) #[[1, 2, 3, 4, 5], [6, 7, 8, 9]]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Alex', 22)
p2 = copy.copy(p1)
p3 = p1
p1.age = 55
print(p1.age) #55
print(p2.age) #22
print(p3.age) #55

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
boss1 = Person('boss', 50)
em1 = Person('Em1', 30)
company1 = Company(boss1, em1)
company_shallow = copy.copy(company1)
company_deep = copy.deepcopy(company1)
company1.boss.name = 'NewBoss'
company1.boss.age = '90'
print(company_shallow.boss.name, company_shallow.boss.age) #NewBoss, 90
print(company_deep.boss.name, company_deep.boss.age) #Boss, 50