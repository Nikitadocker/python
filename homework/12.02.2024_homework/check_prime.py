import math
def check_prime(number_to_check):
    if number_to_check == 2 or number_to_check == 3:
        check_result ="Prime"

            
    else:
        check_result='Not Prime and Composite'    
        initial_devider = 2
        final_devider = math.isqrt(number_to_check)  # final_devider = 1
        deviders = range(initial_devider, final_devider +1)  # deviders = [2]
        for current_devider in deviders:
            if number_to_check % current_devider == 0:
                check_result='Composite'
                break
            else:
                check_result='Prime'
        
    return check_result 