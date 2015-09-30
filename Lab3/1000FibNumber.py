var = 2
start = 1
last = 1
while(len(str(start)) < 1000):
    var=var+1

    temp = start
    start = start+last
    last = temp

print("Final: " + str(var))
