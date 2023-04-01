# Lets perform an exponent: (2^3) using for loop: 2*2*2
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


answer = raise_to_power(2, 5)
print(answer)
