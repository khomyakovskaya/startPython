#Определяется рандомное число от 1 до 10
#Пользоатель вводит число
#Сравниваются числа больше/меньше
#Количество попыток ограничено

import random
random_number = random.randint(1,100)
tries = 1
user_number = int(input("\n Введите число от 1 до 100\n"))
while random_number!=user_number and tries < 5:
    if random_number > user_number:
        print("Введенное число меньше")
    elif random_number < user_number:
        print("Введенное число больше")
    if 5 - tries != 1:
        print("\n У Вас осталось", 5 - tries, "попытки")
    else:
        print("\n У Вас осталась", 5 - tries, "попытка")
    user_number = int(input("\n Повторите попытку\n"))
    tries +=1
print("Вы использовали все попытки")
print("Загаданное число -", random_number)
if random_number == user_number and tries <= 5:
    print("Ваше предположение верно")
    if tries == 5:
        print("\n Вам понадобилось", tries , "попыток")
    elif tries == 1:
        print("\n Вам понадобилфсь", tries , "попытка")
    else:
        print("\n Вам понадобилось", tries , "попытки")