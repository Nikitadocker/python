import json
from check_prime import check_prime

big_to_small_letters = {
    "Composite": "composite",
    "Prime": "prime",
    "Not Prime and Composite": "not prime and composite",
}

math_eng_ru_translation = {
    "composite": "составное",
    "prime": "простое",
    "not prime and composite": "и простым, ни составным",
}

with open("output_pids.json", "r+") as file:

    file_check = json.load(file)  # <class 'list'>


for key in file_check:
    result_before_check = key["Is Prime"]

    process_id = key["Process Number"]

    result_after_check = check_prime(int(process_id))

    process_name = key["Processs Name"]

    if result_before_check != result_after_check:
        print(
            "Pid процесса с именем {0} проверен. Найдена ошибка. Число {1} на самом деле {2}, а в файле написано {3}".format(
                process_name,
                process_id,
                math_eng_ru_translation[big_to_small_letters[result_after_check]],
                math_eng_ru_translation[big_to_small_letters[result_before_check]],
            )
        )
