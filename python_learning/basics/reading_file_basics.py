#! /utc/bin/python3 

from doctest import testfile


testFile = open("/home/wojnaja/learning/python_learning/help_files/reading_basics.txt", "r")#we have different modes
#r (read, only sees whats in the file)
#w (write, we can write to the file)
#a (append, we can read, write and add to the file)
#r+ (read and write, we can read and overwrite the file)
#readable = print(testFile.readable())# this will return boolean if its readable or not
print(testFile.read())
#.readline - will read only first line of the file, if we put it 2 times it will print the line below, because it moves cursor. 
#print(testFile.readline())#moves the cursor to the 2nd line
#print(testFile.readline())#prints 2nd line 
#we can use .readlines and it will create all lines and put it into a list
#print("part 2")
#print(', '.join(testFile.readlines()))
testFile.close()#when we open the file, we have to close it, once we are done reading it, in our case loading to variable testFile
