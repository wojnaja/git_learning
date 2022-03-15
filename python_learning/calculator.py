#! /usr/bin/python3
from math import*
num1 = float(input("Enter your first number: "))
operator_list =       [" +   ","  -   ","  *   ","  /   ","    ^   "]
operator_list_index = ["(0)","    (1) ","  (2)","   (3)", "   (4)  "]
print('   '.join(operator_list)) #will pirnt the output without brackets nor quotation marks
print('   '.join(operator_list_index))
op = input("Select operator from the list: ")


#op = input("Enter your operator: ")
num2 = float(input("Enter your second number: "))

if op == "0":
    print("The result of your operation \"+\" is: " + str((num1 + num2)))
elif op == "1":
    print("The result of your operation \"-\" is: " + (str(num1 - num2)))
elif op == "2":
    print("The result of your operation \"*\" is: " + (str(num1 * num2)))
elif op == "3":
    print("The result of your operation \"/\" is: " + (str(num1 / num2)))
elif op == "4":
    power = (pow(num1,num2))
    print("The result of your operation \"^\" is: " + (str((power))))
else:
    print("invalid operator, select from 0 - 4")
