

def split_array(array):
	left_array = []
	left_array = array[0:len(array)//2]

	right_array = []	
	right_array = array[len(array)//2:len(array)]

	array = [left_array, right_array]

	return array
	



file = [45, 34, 2, 34, 67, 3, 43]
n = len(file)



while n > 2:
	
	file = split_array(file)
	n = len(file[0])

	for i in range (len(file[0]):
		file_tmp += split_array(file[0])


	print (file)
	print (len(file[0]))
	