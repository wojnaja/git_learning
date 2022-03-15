print("Part1")
is_male = True
is_tall = True

if is_male or is_tall: 
    print("You are a male or tall or both !")
else:
    print("You are neither male nor tall!")#nothing from variables is true


print("Part2")
is_male = True
is_tall = False

if is_male and is_tall: 
    print("You are a tall male!")
else:
    print("You are not a tall male!")#nothing from variables is true

print("Part3")
is_male = False
is_tall = True

if is_male and is_tall: 
    print("You are a tall male!")
elif is_male and not(is_tall): #if you want to check if they are male but not tall, we se else if = elif 
    print("You are a short male")
elif is_tall and not(is_male):
    print("You are a tall female")
else:
    print("You are not a tall male!")#nothing from variables is true