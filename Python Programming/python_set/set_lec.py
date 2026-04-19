# sets are unordered hence,output will be in any order & can't be defined
thisset = {"apple", "banana", "cherry"}
print(thisset)

# duplicate values not allowed in sets. it will simply ignore the duplicate value
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# here True & 1 is treated as dupliacte value in sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# data type of set
myset = {"apple", "banana", "cherry"}
print(type(myset))

# set keyword to create a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print(type(thisset))

# check if specified value is in set or not using in keyword
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# loop through set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# add() method in sets add one item to the existing set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update() method in sets add items from one set to another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# object in update() method can be any iterable objects
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)