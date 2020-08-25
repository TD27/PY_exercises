
# Sorting - Bubble Sort

# Functions
def return_bigger(x, y):
	if x >= y:
		return x
	else:
		return y
		
def return_smaler(x, y):
	if x < y:
		return x
	else:
		return y

def return_swap (x,y):
	if x < y:
		return True
	else:
		return False

# Import of Modules
import random


# Initialization of random file
file = []
for var in range (100):
	file.append(random.randint(1,100))

# Definition of variables
bigger = 0
smaler = 0
var_1 = 0
var = 0
first= 0
iteration = 0
swap = True



print (file)

swap = False
for var in range(len(file)-1):

	swap = return_swap(	file[var], file[var + 1]) #compare values of two numbers
	
	while swap:
		bigger = return_bigger(file[var], file[var + 1])
		smaler = return_smaler(file[var], file[var + 1])
		file[var] = bigger
		file[var+1] = smaler
		iteration += 1
		if var == 0: #control of the end of the file
			swap = False
		else:
			swap = return_swap(file[var-1], file[var]) #check values of previous numbers
			var -= 1
		print (file)
		
print ("number of interations: ", iteration)
print ("end")

