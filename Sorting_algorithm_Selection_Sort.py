# Sorting algorithm - Selection Sort

# Functions


# Import of Modules
import random


# Initialization of random file
file = []
for var in range (50):
	file.append(random.randint(1,100))


# Definition of variables
iteration = 0
final_file = []


#Core code
print (file)

for var in range(len(file)-1):
	final_file.append(max(file))
	file.remove(max(file))
	print (final_file)
	iteration += 1

		
print ("number of interations: ", iteration)
print ("end")


