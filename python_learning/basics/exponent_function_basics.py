#! usr/bin/python3

print(2**3)#2^3

#doing the same with using for loop

print("******PART 2****************")
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


base_num = int(input("Insert base number: "))
pow_num = int(input("Insert pow number: "))
print(raise_to_power(base_num,pow_num))