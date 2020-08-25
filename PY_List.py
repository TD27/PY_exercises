# List
#
#words = ["Hello", "world", "!"]
#print(words[0])
#print(words[1])
#print(words[2])

# print certain item of the list
#number = 3
#things = ["string", 0, [1, 2, number], 4.56]
#print(things[1])
#print(things[2])
#print(things[2][2])
#print(things[3])
#print(things[0][2]+things[0][4])


# reassign certain item of the list
#nums = [7, 7, 7, 7, 7]
#nums[2] = 5
#print(nums)


column = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

x = 0
while x <= 4:
	y = 0 
	while y <= 4:
		column[x][y] = int(input("Zadej číslo: "))
		print ("[",x,",", y,"] = ",column)
		y += 1
	x += 1
print ("konec")
print (column)


# List operations
#nums = [1, 2, 3]
#print(nums + [4, 5, 6])
#print(nums * 3)


#x = input ("Input a number: ")
#print (x)


# List operations: in, not in
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# List method: .append ... add item to the end of the existing list
nums = [1, 2, 3]
nums.append(4)
print(nums)

# List function: len ... returns number of items in the list
nums = [1, 3, 5, 2, 4]
print(len(nums))

# List method: .insert ... insert item to the list at the given position of index
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)


# There are a few more useful functions and methods for lists. 
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# len(list): Returns number of items in the list
#
#list.count(obj): Returns a count of how many times an item occurs in a list
#list.remove(obj): Removes an object from a list
#list.reverse(): Reverses objects in a list
#list.index(obj): Returns index of the object
#list.append(obj): Add object at the end of the list
#list.insert(index,obj): Insert the object at the index position
#list.extended(list): Add new list at the end of the original list
#
#
#append() - Add an element to the end of the list
#extend() - Add all elements of a list to the another list
#insert() - Insert an item at the defined index
#remove() - Removes an item from the list
#pop() - Removes and returns an element at the given index
#clear() - Removes all items from the list
#index() - Returns the index of the first matched item
#count() - Returns the count of number of items passed as an argument
#sort() - Sort items in a list in ascending order
#reverse() - Reverse the order of items in the list
#copy() - Returns a shallow copy of the list

