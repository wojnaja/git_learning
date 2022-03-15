#helps you organize your code, once needed, can be "called"

#function, that says hi to a user - to whoever is running a program



#if python sees "def", he knows we want to use a function
#everything in the functions, needs to be indented - if its not, it wont work and its not considered as a function
def sayhi():
    print("Hi user, how you doing?")
    print("I am learning python bruh!")

#function code is not getting executed by default
#to execute it, we just need to type the name of the function

#python goes in order, so it will first print "top", then jumps up to run "say_hi" function, then goes to another line and says "bottom"
print("top")
sayhi()
print("bottom")

#we can add additional information to a fucntion - called parameter

def say_fuck(name): #we need to specify a name for using this function, so when calling the function we need to put a name/parameter to the bracket
    print("Hey " + name + "!")
    print("Go fuck youreself!")

say_fuck("Steve")
say_fuck("Mike")

print()
print()
print()
print()
print()

def say_fuck2(test_say_fuck): #we need to specify a name for using this function, so when calling the function we need to put a name/parameter to the bracket
    print("Hey " + test_say_fuck + "!")
    print("Go fuck youreself!")


test_say_fuck = input("Hi, what is your name ?:")
say_fuck2(test_say_fuck)


