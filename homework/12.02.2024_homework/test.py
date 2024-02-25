import json
from check_prime import check_prime

# big_to_small_letters = {
#     "Composite": "composite",
#     "Prime": "prime",
#     "Not Prime and Composite": "not prime and composite",
# }

# math_eng_ru_translation = {
#     "Composite": "Cоставное",
#     "Prime": "Простое",
#     "Not Prime and Composite": "Ни Простым, ни Составным",
# }


math_eng_ru_translation = {
    False: "Cоставное",
    True: "Простое",
    "Not Prime and Composite": "Ни Простым, ни Составным",
}


with open("output_pids.json", "r+") as file:

    file_check = json.load(file)  # <class 'list'>


for key in file_check:
    result_before_check = key["Is Prime"]

    process_id = key["Process Number"]

    result_after_check = check_prime(int(process_id))

    process_name = key["Processs Name"]

    if result_after_check == "Prime":

        result_after_check = True
    else:
        result_after_check = False

    # print(result_before_check)

    # print(result_after_check)

    if result_before_check != result_after_check:
        print(
            "Pid процесс с именем {0} проверен. Найдена ошибка. Число {1} на самом деле {2}, а в файле написано {3}".format(
                process_name,
                process_id,
                math_eng_ru_translation[result_after_check],
                math_eng_ru_translation[result_before_check],
            )
        )

    # if result_before_check != result_after_check:
    #     print(
    #         "Pid процесса с именем {0} проверен. Найдена ошибка. Число {1} на самом деле {2}, а в файле написано {3}".format(
    #             process_name,
    #             process_id,
    #             math_eng_ru_translation[result_after_check].lower(),
    #             math_eng_ru_translation[result_before_check].lower(),
    #         )
    #     )
