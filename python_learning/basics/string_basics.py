print("Ucim\"se python") #\ se pouziva pro upravy stringu, pokud chceme napriklad zapsat ", normalne by to ukoncilo string, pokud zapiseme za \ tak to pujde. 

phrase = "test"
print(phrase + " is cool") #concatenation < spojeni vice textu dohromady, muzeme spojovat take nekolik phrase viz nize

phrase = "testtttttttttd"
phrase2 = "test2"
print(phrase + " " + phrase2)


print(phrase.upper()) #pouzvame funkce, upper pro uppercase, lower pro lowercase 
print(phrase.upper().isupper())#muzeme pouzit isupper < hodi false/true value na zaklade toho jestli je upper nebo lower


testovaci_phrase = "TeStUjU"
print(len(testovaci_phrase)) #nam vrati cislo, jak dlouha je phrase 
print(testovaci_phrase[0])#[index] nam vrati cislo podle indexu, 0 znamena prvni (0,1,2,3...)
print (testovaci_phrase.index("U"))#nam vrati cislo indexu - U je na ctvrtem miste, proto nam to hodi U
print(testovaci_phrase.replace("Te","ko"))
