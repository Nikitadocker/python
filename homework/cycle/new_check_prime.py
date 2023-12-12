# number = int(input())
# prime = True
# for i in range(2,  int(number ** 0.5) + 1):
#     if number % i == 0:
#         prime == False
#         print("Число", number, "cоставное")
#         break
#     if prime == True:
#         print("Число", number, "простое")


number = int(input())
prime = True
for i in range(2,  number):
    if number % i == 0:
        prime = False
        break
if prime == True:
    print("Число", number, "простое")
else:
    print("Число", number, "cоставное")
