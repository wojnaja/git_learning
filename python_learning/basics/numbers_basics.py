
from math import *#je potreba pokud chceme pouzit nejake dalsi math funkce viz line 22
my_num = -5
print(my_num)

print(2)
print(2.95459)
print(-32923)
print(3 + 4.5)
print(3*4+5)
print(3+5*5)
print(10 % 3)#10 deleno 3 a vyhodi nam to zbytek po deleni cte se jako "modulus"


#muzeme prevest cislo na string
print(str(my_num) + " is my favourite number")#pokud chceme napsat cislo za string, musime prevest na string, jinak to nepujde 
print(abs(my_num))#vrati absolutni hodnotu, napr misto -5 > 5
print(pow(3,2))#pow se pouziva jako "na x-tou" > 3na2 = 9
print(max(4,6,10, 12131, 2,5))#vypise maximalni hodnotu, umi i min 
print(round(3.35)) #zaokrouhluje

print(floor(3.7))#odebere decimal 
print(ceil(3.6))#zaokrouhli nahoru
print(sqrt(9))#odmocnina, vrati hodnotu 3.0
print(floor(sqrt(9)))#vrati hodnotu 3, protoze odebereme .0