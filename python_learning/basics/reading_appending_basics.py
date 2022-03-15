#! /usr/bin/python3 


print("This will print the entire file list.")
testFile = open("/home/wojnaja/learning/python_learning/help_files/reading_basics.txt", "r")
print(testFile.read())
testFile.close()

print("We want to add another item to the list.")
testFile2 = open("/home/wojnaja/learning/python_learning/help_files/reading_basics2.txt", "a")
#if we run it accidentaly, it can mess up the file.
testFile2.write("\nTest 7")#if we want to add something to the new line instead behind the last line, we need to put \n 
testFile2.close()

print("We want to over/write a file")
testFile3 = open("/home/wojnaja/learning/python_learning/help_files/reading_basics3.txt", "w")
print(testFile3.write("test1"))
testFile3.close()