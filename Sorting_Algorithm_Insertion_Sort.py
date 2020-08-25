# Sorting Algorithm - Insertion Sort

# functions
def return_sorted(sorted_array, x):
	for i in range (len(sorted_array)):
		if x > sorted_array[i]:
			sorted_array.insert(i, x)
			return sorted_array
	sorted_array.append(x)
	return sorted_array


# Import of Modules
import random


# Initialization of random file
file = []
for var in range (100):
	file.append(random.randint(1,100))


# Definition of variables
iteration = 0


#Core code

print (file)

final_file = []
#final_file.append(file[0])

for var in range(len(file)-1):
	final_file = return_sorted(final_file,file[var])
	print (final_file)
	iteration += 1

		
print ("number of interations: ", iteration)
print ("end")

