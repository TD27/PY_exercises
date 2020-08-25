


# Import of Modules
import random
import time



# Sorting - Bubble Sort
def bubble_sort(file):
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

	# Definition of variables
	bigger = 0
	smaler = 0
	var_1 = 0
	var = 0
	first= 0
	iteration = 0
	swap = True

	# Start time
	start_time = time.time()

	# Core code - Bubble Sort
#	print ("========== Bubble Sort ==========")
#	print ("start time: ", start_time)
#	print (file)

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
	#		print (file)

	# end time
	end_time = time.time()		
	total_time = end_time - start_time		

#	print (file)		
#	print ("number of interations: ", iteration)
#	print ("duration: ", total_time)
#	print ("========== end ==========")

	return iteration, start_time, end_time, total_time

# Sorting Algorithm - Insertion Sort
def insertion_sort(file):
	# functions
	def return_sorted(sorted_array, x):
		for i in range (len(sorted_array)):
			if x > sorted_array[i]:
				sorted_array.insert(i, x)
				return sorted_array
		sorted_array.append(x)
		return sorted_array


	# Definition of variables
	iteration = 0
	final_file = []

	# Start time
	start_time = time.time()

	#Core code
#	print ("========== Insertion Sort ==========")
#	print ("start time: ", start_time)

	for var in range(len(file)-1):
		final_file = return_sorted(final_file,file[var])
	#	print (final_file)
		iteration += 1


	# end time
	end_time = time.time()		
	total_time = end_time - start_time			

#	print (final_file)		
#	print ("number of interations: ", iteration)
#	print ("duration: ", total_time)
#	print ("========== end ==========")

	return iteration, start_time, end_time, total_time


# Sorting Algorithm - Selection Sort
def selection_sort(file):
	# Definition of variables

	iteration = 0
	final_file = []

	# Start time
	start_time = time.time()

	#Core code

	for var in range(len(file)-1):
		final_file.append(max(file))
		file.remove(max(file))
	#	print (final_file)
		iteration += 1


	# end time
	end_time = time.time()		
	total_time = end_time - start_time			

#	print (final_file)		
#	print ("number of interations: ", iteration)
#	print ("duration: ", total_time)
#	print ("========== end ==========")

	return iteration, start_time, end_time, total_time



# ====================================
# ====== Algorithm Comparison ========
# ====================================

file_init = []
file_size = 2000

for file in range(0,file_size,100):

	# Initialization of random file
	for var in range (file):
		file_init.append(random.randint(1,file))

	print ("File size: ", file)
	print ("Bubble Sort:", bubble_sort(file_init))
	print ("Insertion Sort", insertion_sort(file_init))
	print ("Selection Sort", selection_sort(file_init))
	print ("===================")



