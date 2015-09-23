val = 1
lastval = 1
ans = 0


while(val < 4000000):

    if(val % 2 == 0):
        ans = ans+val
    
    temp = val
    val = val+lastval
    lastval = temp

print ("Final: " +  str(ans))

