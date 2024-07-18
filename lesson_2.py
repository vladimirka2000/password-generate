from random import choice



passwords = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

question_1 = int(input("Сколько символов будет в вашем пароле?"))

result = ""

for i in range(question_1):
    result += choice(passwords)

print(f"Ваш пароль {result}")

