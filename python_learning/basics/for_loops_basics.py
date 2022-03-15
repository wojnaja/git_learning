#! usr/bin/python3

print("******PART 1****************")
for letter in "Chlupaty pero": #for each letter in string, print letter 
    print(letter)


print("******PART 2****************")
friends = ["Jakub","Kokot","Pica"]

for friend in friends:
    print(friend)

print("******PART 3****************")
for index in range(10): #not going to print out the last number, because we start at 0
    print(index)

print("******PART 4****************")
for index in range(1,11): #not going to print out the last number
    print(index)

print("******PART 5****************")
for index in range(len(friends)): #another way how to display list printed using for loop
    print(friends[index])
    
print("******PART 6****************")
for index in range(5): #not going to print out the last number, because we start at 0
    if index == 0:
        print("first iteration")
    else:
        print("Not first")