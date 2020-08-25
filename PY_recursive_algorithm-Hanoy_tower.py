#---------------------------------------------
#----- HANOI TOWER - recursive algorithm -----
#---------------------------------------------


# Recursive function
def tower (n, beg, end, aux):
	if n == 1:
		end.append(beg.pop())
		print (beg, end, aux)
		return beg, end, aux
	else:
		tower (n-1, beg, aux, end)
		tower(1, beg, end, aux)
		tower (n-1, aux, end, beg)
		return A, B, C


# Definition
A = [5, 4, 3, 2, 1]
B = []
C = []


# Core code
print (A, B, C)
print (tower(len(A), A, C, B))
