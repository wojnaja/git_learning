print("*****************************PART 1***************************************")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
        #print(str(num1) + " is the biggest number")
    elif num2 >= num1 and num2 >= num3:
        #print(str(num2) + " is the biggest number")
        return num2
    else:
        return num3
        #print(str(num3) + " is the biggest number")

num1 = input("Insert first number to compare:")
num2 = input("Insert second number to compare:")
num3 = input("Insert third number to compare:")
print(max_num(num1,num2,num3))

# we can do the same with strings
# == means equal, to see if both values are equal 
# != means not equal
# <= less than or equal to
# >= more than or equal to
