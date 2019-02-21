#Using a list as a stack

#The stack abstract data structure is widely used in computer science. 
#This collection is implemented to best fit the LIFO principle ( last in, first out ). 
#Sometimes we need one data structure that behaves in such a manner.

#Even though python does not provide a special stack data structure, list's can easily be used in the scope.


stack = [1,2,3]
stack.append(4)
# adds 4 at the end
stack.append(5)
print(stack)
#>>> [1, 2, 4, 5]
# removes and return last element
print(stack.pop())
#>>> 5

