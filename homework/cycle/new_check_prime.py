number = int(input())
prime = True
for i in range(2,  int(x**0, 5) + 1):
    if number % i == 0:
        prime == False
        print("Число", number, "cоставное")
if prime == True:
    print("Число", number, "простое")
