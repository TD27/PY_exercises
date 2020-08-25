
import time



#print ("======== RECURSION ===========")
def recursion(total_value, interest, length):
	start_time = time.time()
	
	def rec_interest(value, x, n):
	#	print ("called with x:", n)
		if n== 1:
			return value + value * 0.01 * x
		else: 
			value =  int(rec_interest(value, x, n-1) + 0.01 * x * rec_interest(value, x, n-1))
	#		print ("recursion: ", n, "res: ", value)
			return value
	
	print ("total value: ",rec_interest(total_value, interest, length))
	end_time = time.time()
	print ("recursion duration: ", end_time-start_time)


#print ("======== FOR ===========")
def for_cycle (total_value, inter, length):
	start_time = time.time()
	
	
	def interest(x, y):
		result = x * 0.01 * y
		return result

	
	A_value = total_value
	
	for i in range (length):
		A_value += int(interest(A_value, inter))
		#print (i, ". year value: ", A_value)
	print ("total value: ", A_value)
	end_time = time.time()
	print ("for cycle duration: ", end_time-start_time)



for len in range (18,23):
	print ("length: ", len)
	recursion(1000000, 6, len)
	for_cycle(1000000, 6, len)
	print ("-------------")