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