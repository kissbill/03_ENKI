#del statement for lists

#Python's del statement has multiple usages when used on lists. 
#It differs from the pop() method because when using del, 
#the element won't be returned when removing it.

#Delete the element at a given index:

a = [ 0, 1, 2, 3 ]
del a[0]
a
#[ 1, 2, 3 ]
#Delete a slice of the list:

a = [ 1, 2, 3, 4 ]
del a[0:2]
a
[ 3, 4 ]
#Note that even though three elements are specified (0,1,2),
#the last one is not deleted. 
#Consider this example, in which nothing happens:

a = [ 1, 2, 3, 4 ]
del a[0:0]
a
#[ 1, 2, 3, 4 ]
#To delete the entire list:

del a[:]
a
#[]
	 0 1 2 3  4  5
e = [7,8,9,11,15,19]
del e[2:4]
print(e)