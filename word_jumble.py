#Компьютер выбирает случайное слово и переставляет буквы
#Задача - угадать слово

import  random
#создаем последовательность слов
WORDS = ("угадай", "слово", "буквы", "перепутаны", "рандомно")
#выбираем случайное слово из созданной последовательности
word = random.choice(WORDS)
count = 0
correct = word

#создаем пустую последовательность
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Угадай слово:", jumble)
guess = input("\nВведите Ваш вариант - ")
while guess != correct and guess != "":
    count += 1
    print("\nПопробуйте еще")
    prompt = input("\nПодсказку?")
    if prompt == "да":
        print("\n", count, "буква -", correct[count - 1])
        guess = input("\nВведите Ваш вариант - ")
    else:
        guess = input("\nВведите Ваш вариант - ")

if guess == correct:
    print("Верно!")

