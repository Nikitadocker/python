import math

startd = 2
finishd = 10
checknumber = startd

while checknumber <= finishd:
    delitel = checknumber
    prime = True

    while delitel <= math.sqrt(checknumber):
        if checknumber % delitel == 0:
            prime = False
            break
        
        delitel += 1
        
    if prime:       
        print(checknumber)
    
    checknumber += 1
