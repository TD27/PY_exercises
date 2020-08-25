# Recursive

print ("==============FACTORIAL===============")

def factorial(x):
	print ("called with x:" + str(x))
	if x == 1:
		return 1
	else:
		res = x * factorial(x-1)
		print ("intermediate result x = ",x, " and factorial (",x ,") = ", res)
		return res

print(factorial(5))
print ("=============================")




print ("=============SUM================")

def sum_to(x):
	print ("called with", x)
	if x == 0:
		return 0
	else:
		res = x + sum_to(x-1)
		print ("intermediate result x = ",x, " and sum (",x ,") = ", res)
		return res
		
print (sum_to(3))
print ("=============================")




print ("============= FIB ================")

def fib(x):
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

print(fib(12))
print ("=============================")




print ("========== EVEN / ODD ============")

def is_even(x):
	print ("is_even - called with: ", x)
	if x == 0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):
	print ("is odd - called with: ",x)
	return not is_even(x)

print(is_odd(5))
print(is_even(5))
print ("=============================")




print ("========== FACTORIAL ============")

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(5))
print ("=============================")



print ("============= test ==============")

def rec_print (n):
	if n == 0:
		return 1
	else: 
		rec_print (n-1)
		print (n)
		return n
		
rec_print(5)
print ("=============================")




