# ==========================================
# It takes out data from given list structure and place it to 
# ==========================================

# Recursive function 		
def take_data (A):
	n = len (A)
	for i in range (n):
		if type (A[i]) == int:
			list.append(A[i])
		else:
			take_data (A[i])
		print (list)
	return


# Definition
array = [1, 2, [10, 20, 30, [100, 200, 300, [1000]]], 4, 5, 6, [10, 20, 30], 7]
n = len (array)
list = []

# Core code
print (array)
take_data (array)

		
