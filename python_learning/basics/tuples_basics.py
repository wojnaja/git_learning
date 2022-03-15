#tuple is similar to a list, structure, when we can store multiple pieces of information 
#For most of the time we will use list, tuples are used in case, that the values WONT BE CHANGED


coordinate = (4, 5)

#tuple is immutable = cant be changed or modified, we cannot remove some of it, we cannot update it, if we have tuple, thats it
#list uses squared brackets and can be modified = is mutable

print (coordinate[0])#we can print out using index as with lists
print (coordinate[1])#we can print out using index as with lists

#we can create a list of tuples

coordinate_list = [(4,5), (5,9)]
print(coordinate_list)
