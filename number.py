#Определяется рандомное число от 1 до 10
#Пользоатель вводит число
#Сравниваются числа больше/меньше

import random
random_number = random.randint(1,100)
tries = 1
user_number = int(input("\n Введите число от 1 до 100\n"))
while random_number!=user_number:
    if random_number > user_number:
        print("Введенное число меньше")
    elif random_number < user_number:
        print("Введенное число больше")
    user_number = int(input("\n Повторите попытку"))
    tries +=1
print("Ваше предположение верно")
print("\n Вам понадобилось", tries , "попыток" )