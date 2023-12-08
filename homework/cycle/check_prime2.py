number = 17
pupa = range(2, number-1)

for i in pupa:
    # if number % i != 0:

    #     i +=1

    if number % i == 0:

        print("Число", number, "являeтся составным")
        break
else:
    print("Число", number, "являeтся простым")


# подправить для составных чисел
