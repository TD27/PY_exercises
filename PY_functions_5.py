def compare (x, y):
    if x > y:
        longer = x
    else:
        longer = y
        alfa = y
    return longer

x = input ("Zadej x:")
y = input ("Zadej y:")
longer = compare (x,y)
print ("Delší je: ", longer)

