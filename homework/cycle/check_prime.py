number = 13
# collection = [2,3,4,5,6,7,8,9,10,11,12]
pupa = range (2,number-1)

for i in pupa:
    if number % i != 0:
        
        i +=1

    else: print ("Число" , number , "являeтся составным")
print ("Число" , number , "являeтся простым")


# подправить для составных чисел