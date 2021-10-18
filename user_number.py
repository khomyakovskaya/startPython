#Пользователь задает число от 1 до 100
#сравниваем загаданное число с 50
#пока загаданное число меньше нашего варианта
#    уменьшаем вариант
#пока больше:
#   увеличиваем

import random
user_number = int(input("Введите число от 1 до 100\n"))
computer_number = 50
tries = 1
while user_number != computer_number:
    if user_number < computer_number:
        computer_number = random.randint(1, computer_number)
        print("Компьютер предположил число -", computer_number)
    else:
        computer_number = random.randint(computer_number, 100)
        print("Компьютер предположил число -", computer_number)
    tries +=1
print(user_number, "загаданное число")
print("Число использованных попыток -", tries)