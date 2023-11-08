import math


start = 2

finish = 10

delimoe = start


while  delimoe <= finish:
    
    delitel = delimoe
    
    while delitel <= math.sqrt (delimoe):
        
        if delimoe % delitel == 0:
            
            continue
        
        print (delimoe)
        
        delitel +1
        
    
    
    
    
    delimoe +=1