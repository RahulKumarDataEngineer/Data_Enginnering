# several ways to join sets , let's see examples one by one.

# WITH HELP OF union() & update() method
# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Use '|' operator to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Join multiple sets using union method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Join multiple sets using | operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# Join a Set and a Tuple
# union() method allows to join set , tuple and  list
x = {"a", "b", "c"}
y = [1, 2, 3]

z = x.union(y)
print(z)

# Update() method
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Intersection ( & operator ) 
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# You can use the & operator instead of the intersection() method, and you will get the same result.

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with 
# the intersection() method.

# example - Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# difference() method / '-' OPERATOR
# it will return a new set that will contain only the items from 1st set that are not present in other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# SYMMETRIC_DIFFERENCE / '^' OPERATOR
# This will return a new set with items that are not present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


# Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)