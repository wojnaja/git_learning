friends = ["Pepa","Karel","Jakub","Marek","Jirka"]
#           0       1        2      3        4
#kazda hodnota v listu ma index, zacinajici od nuly
print(friends)
print()
print()
print(friends[1]) #pokud dame cislo indexu do hranate zavorky, vyhodi nam to pouze hodnotu Karel
print(friends[1:]) # v pripade, ze pouzijeme [index:], tak vypise vsechny cleny od indexu 1
print(friends[1:4]) # v pripade, ze pouzijeme [index:index] tak vypise rozsah od do 

#index muzeme take zmenit - friends[1] = "kokot - nahradi hodnotu v listu na kokot
list1 = ["Pepa","Karel","Jakub","Marek","Jirka"]
print(list1)
print()
list1[1] = "kokot"
print(list1)