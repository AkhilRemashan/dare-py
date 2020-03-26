lucky_numbers = [2, 6, 28, 69, 91]
friends = ["Aaron", "Betty", "Calvin", "Daisy", "Eric", "Betty"]

# appending two lists
friends.extend(lucky_numbers)

# individual addition
friends.append("Franky")

friends.insert(1, "Bob")
friends.remove("Daisy")
# friends.clear()


friends.pop() # pops out last element

print(friends.index("Aaron")) # tells the index position
print(friends.count("Betty")) # tells total number

lucky_numbers.sort()
lucky_numbers.reverse() # reverse list

friends2 = friends.copy() # makes copy of list

print(lucky_numbers)
print(friends)
print(friends2)
