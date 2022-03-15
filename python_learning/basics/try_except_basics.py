#! /usr/bin/python3


try:
    
    number = int(input("Enter your number: ")) #only number is expected, if we put string, program fails - this is not wanted, we can use something called try-except
    print(number)
    value = 10/0
except ZeroDivisionError as err: #if the users puts something wrong - in this case string instead of number, our program will print out "invalid input" message
    print(err)
#if we put only "except", its too broad and it will show "invalid input" for all errors within try block, best practice is to use specific error 
except ValueError:
    print("Invalid value")



