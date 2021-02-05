thislist = ["apple", "banana", "cherry"]
print(thislist)

#List length
print(len(thislist))

#List Type
print(type(thislist))

nextlist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(nextlist)

"""
COLLECTIONS (ARRAYS)

    List            is a collection which is ordered and changeable. Allows duplicate members.
    Tuple           is a collection which is ordered and unchangeable. Allows duplicate members.
    Set             is a collection which is unordered and unindexed. No duplicate members.
    Dictionary      is a collection which is unordered and changeable. No duplicate members.
"""

#Much like strings are arrays things can be selected from the array in multiple ways. 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#Check if exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#Changing List items.
thislist[1] = "blackcurrant"
print(thislist)

#Change Range of items
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Replacing an Array 
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Unlike above this would insert an Array so that it is nested inside of the array. 
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)

#Doing the following essentially removes indexs 1 and 2 and then replaces them with "watermelon" then resizes the array. 
thislist[1:3] = ["watermelon"]
print(thislist)

#Inserting without changing data already in the list. Adds in in the index given moving everything else down. 
thislist.insert(2, "watermelon")
print(thislist)

#append
thislist.append("orange")
print(thislist)

#extend - this works with any other type of array. 
tropical = ["mango", "pineapple", "papaya", "banana"]
thislist.extend(tropical)
print(thislist)

#remove
thislist.remove("banana")
print(thislist)

#pop - remove specific index (if index not specified then will remove the last index)
thislist.pop(1)
print(thislist)

# clear
thislist.clear()
print(thislist)

#del same as pop - can also be used to remove the entire list - this removes the defined list. 
del thislist

"""
LOOPS
"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#using range and len
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#shorthand for loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]