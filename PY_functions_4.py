def distance_from_zero (x):
    if type (x) == Int or type (x) == Float:
        print (x)
        return "Yes"
    else:
        print ("it is:", x)
        return "Nope"
    return


string = input ("Zadej string: ")
print (distance_from_zero (string))
