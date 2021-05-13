
#Sort
s1 = [1,7.0,-3.78, 17]
s2 = [1,7.0,-3.78, 17]
s1.sort() #sort original list
print(s1)
print(sorted(s2)) # create a new list , can be tuple, list
print(s2) #still same and not sorted

#new list
new_list1 = [0]*8
new_list2 = [1]*5
print(new_list1)
print(new_list1+new_list2)

#slicing
slice_list = [1,2,3,4,5,6,7,8]
print(slice_list[1:5]) #[2, 3, 4, 5]
print(slice_list[:6]) #[1, 2, 3, 4, 5, 6]
print(slice_list[3:]) #[4, 5, 6, 7, 8]
print(slice_list[::2]) #[1, 3, 5, 7]
print(slice_list[::-1]) #[8, 7, 6, 5, 4, 3, 2, 1]

#copy
c1 = [1,5,9,1.0,"test"]
c2 = c1 #has same list
c2.append("new")
print(c2)
print(c1) #c1 c2 are same
c3 = c1.copy()
c3.append("another")
print(c3)
c4 = c1[:] #new list
c4.append("another another")
print(c4)

#express
e1 = [1,2,3,4,5,6]
e_square = [i*i for i in e1]
print(e_square) #1, 4, 9, 16, 25, 36]

#unpacking
first, *rest, last = e1
print(first) #1
print(rest) #list: [2, 3, 4, 5]
print(last) #6


