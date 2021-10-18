#Подбрасывается монетка 10 раз
#Рассчитать сколько раз выпадет орел, а сколько решка

import random
tries = 0
tails = 0
eagle = 0
money = random.randint(0,1)
while tries < 100:
    if money == 1:
        eagle +=1
    elif money == 0:
        tails += 1
    tries += 1
    money = random.randint(0, 1)
print("Орел выпал", eagle, "раз")
print("Решка выпала", tails, "раз")