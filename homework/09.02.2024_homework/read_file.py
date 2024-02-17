import json
from check_prime import check_prime

with open("output_pids.json", "r+") as file:

    file_check = json.load(file)  # <class 'list'>


for key in file_check:
    prime_or_composite = key["Prime or Composite"]

    pid_for_check = key["pid_number"]

    result_after_check = check_prime(int(pid_for_check))

    if result_after_check == "Prime" and prime_or_composite != "Prime":
        print(
            "Число, {0} проверено. Найдена ошибка. Значениe в файле {1}, а число должно быть простым".format(
                pid_for_check, prime_or_composite
            )
        )
    elif result_after_check == "Composite" and prime_or_composite != "Composite":
        print(
            "Число, {0} проверено. Найдена ошибка. Значение в файле {1}, а число должно быть составным".format(
                pid_for_check, prime_or_composite
            )
        )
