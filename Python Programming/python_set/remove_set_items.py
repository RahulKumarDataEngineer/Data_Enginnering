# to remove an item from a set use remove() method / discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# # if item to remove doesnot exist then remove() method will raise an error.
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("mango")
# print(thisset)

# but if item to remove doesnot exist then discard() method will not raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("mango")
print(thisset)

# pop() method in set will randomly remove one item from set
# and the returned value of the pop method will be the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear method will empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)