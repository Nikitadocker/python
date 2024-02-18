import json
from check_prime import check_prime

pupa = "Composite"
math_eng_ru_translation = {pupa: "составное", "Prime": "простое"}

with open("output_pids.json", "r+") as file:

    file_check = json.load(file)  # <class 'list'>


for key in file_check:
    result_before_check = key["Prime or Composite"]

    process_id = key["pid_number"]

    result_after_check = check_prime(int(process_id))

    process_name = key["pid_name"]

    if result_before_check != result_after_check:
        print(
            "Pid процесса с именем {0} проверен. Найдена ошибка. Число {1} на самом деле являеться {2}, а в файле написано {3}".format(
                process_name,
                process_id,
                math_eng_ru_translation[result_after_check],
                math_eng_ru_translation[result_before_check],
            )
        )
