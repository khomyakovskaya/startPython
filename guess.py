#Компьютер выбирает слово, сообщает количество букв, дает 5 попыток угадать
#Пользователь должен угадать это слово
#Компьютер отвечает да или нет, есть буква в слове или нет

import random

WORDS = ("словарь",
         "пользователь",
         "компьютер",
         "слова",
         "молодец")

word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("\nВ слове - ", len(correct), "букв")
print("\nТы можешь 5 раз спросить меня, есть ли буква в этом слове")

for a in range(5):
    i = input("\nКакую букву проверим?")
    if i in correct:
        print("\nТакая буква есть")
    else:
        print("\nТакой буквы в этом слове нет(")

guess = input("\nКакое слово загадано?")

if guess == correct:
    print("Верно!")
else:
    print("Не угадал(((((")


