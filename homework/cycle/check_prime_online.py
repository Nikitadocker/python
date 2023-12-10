number = int(input())

diapozon = range(2, number-1)

for i in diapozon:
    if  number % i  == 0:
        print("Число number являеться составным")
        break
    
else: print("Число number являеться простым")