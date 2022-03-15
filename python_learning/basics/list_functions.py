friends = ["Pepa","Karel","Jakub","Marek","Jirka"]
lucky_numbers = [3, 1, 50, 13, 1050]

print(friends)
print(lucky_numbers)

friends.extend(lucky_numbers) #spoji listy dohromady, takze vypise lucky_numbers za friends 
print(friends)
friends.append("Martin") #append funkce prida dalsiho clena na konec listu 
print(friends)
friends.insert(1,"Filip") #insert funkce prida clena na misto indexu a zbytek bude posunut
print(friends)
friends.remove("Filip") #remove odebere specifikovaneho clena
print(friends)
friends.pop() #vymaze posledniho clena
print(friends)
friends.clear()#vymaze vsechny cleny v listu
print(friends)
#
#
#
print()
print()
print()
friends = ["Pepa","Karel","Jakub","Marek","Jirka","Jirka","Jirka"]
print(friends.index("Jakub"))#vypise cislo indexu specifikovaneho clena, pokud neni v listu, dostaneme error
print(friends.count("Jirka"))#vypise cislo, kolikrat se specifikovany clen objevi v listu
friends.sort()#seradi list od podle abecedy/od nejmensiho v pripade cisel
print(friends)


list2 = friends.copy()#okopiruje cely list 
print(list2)

print("***********List modification****************************")
print("list without any modification")
test_list = ["Dog", "cat","penis","vagina"]
print(test_list)
print("list with join function used")
print('  '.join(test_list))#means, that i want to use 2 spaces  as a delimiter sign
print('-'.join(test_list))#means, that i want to use -  as a delimiter sign
print(', '.join(test_list))#means, that i want to use -  as a delimiter sign



