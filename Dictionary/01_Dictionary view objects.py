#Dictionary view objects

#An interesting feature python provides 
#for dictionaries are view objects which can be generated using 
#any of the following methods:

#dict.keys()
# returns a new view of dictionary's keys
#dict.values()
# returns a new view of dictionary's values
#dict.items()
# returns a new view of dictionary's items
# items are (key, value) pairs

#The view objects are dynamically tied to the parent dictionary. 
#When the parent dictionary is changed this changes are visible in the view objects too.

#The number of entries in a dictionary can be easily obtained using len(dictview) method:

a = {'one':1, 'two':2, 'three' : 3}
keys = a.keys()
print(len(keys))
#2

#One reason for using view objects is that iteration over a dictionary 
#is more efficient then using lists for this purpose. 
#Dictionary's iter() method works on dictionary views, 
#returning an iterator over keys, values or items:

print(iter(keys))
# iterator over keys is returned
#Also view objects provide efficient ways to perform containment tests and set-like operations 
#( eg. Intersections, Differences, etc. )
 #The in keyword for testing collection membership,
 #can be used both on dictionaries and dictionary views:

print('one' in keys)
#True
print('three' in keys)
#False