
def bigger_left (first,second):
    if first > second:
        return first
    else:
        return second
    

A=(2,12,4,5)
for n in range (len (A)):
    higher = bigger_left (A[n],A[n+1])
    print (higher)

