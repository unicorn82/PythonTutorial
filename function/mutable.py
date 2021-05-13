def foo(x):
    x = 5

var = 10 # immutable type
foo(var)
print(var)

def foo2(a_list):
    a_list.append(10)
    a_list[0] = 0

my_list = [1,2,3,4]
foo2(my_list) # list is mutable and can be changed
print(my_list) #[0, 2, 3, 4, 10]

def foo_rebind(a_list):
    a_list = [100, 200, 300]
    a_list.append(400)

my_list2 = [1,2,3,4]
foo_rebind(my_list2) #list is re-assigned to new list in function, so global list has no change
print(my_list2)  #[1, 2, 3, 4]

def foo_rebind2(a_list):
    a_list = a_list + [100, 200, 300] #list is re-assigned
    a_list.append(400)

my_list3 = [1,2,3,4]
foo_rebind2(my_list3) #list is re-assigned to new list in function, so global list has no change
print(my_list3) #[1, 2, 3, 4]

def foo_not_rebind(a_list):
    a_list +=  [100, 200, 300]
    a_list.append(400)

my_list4 = [1,2,3,4]
foo_not_rebind(my_list4) #list is not re-assigned in function
print(my_list4) #[1, 2, 3, 4, 100, 200, 300, 400]
